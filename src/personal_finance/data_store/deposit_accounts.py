from pathlib import Path

import polars as pl
# import pandas as pd

from personal_finance.configuration.data_config import (
    DataConfig,
    DepositAccountDataConfig,
    load_config_dict_from_yaml,
    load_env,
    EnvName,
    resolve_config_dir_from_env,
    resolve_data_root_dir_from_env,
)
from personal_finance.utils.utils import StrMixin, find_files_in_dir


class DepositAccountDataStore(StrMixin):
    def __init__(self, deposit_account_data_config: DepositAccountDataConfig, entity_name: str):
        self.deposit_account_data_config = deposit_account_data_config
        self.entity_name = entity_name

    def get_account_data_dir_paths(self) -> list[Path]:
        deposit_account_data_config = self.deposit_account_data_config
        dir_paths = [
            Path(deposit_account_data_config.root_dir) / Path(deposit_account_data_config.entity_dir) / Path(sub_dir)
            for sub_dir in self.deposit_account_data_config.sub_dirs
        ]

        return dir_paths

    def get_account_data_file_paths(self) -> list[Path]:
        data_dir_paths = self.get_account_data_dir_paths()

        files = []
        for dir_path in data_dir_paths:
            files.extend(find_files_in_dir(dir_path, ext=".csv"))
            files.extend(find_files_in_dir(dir_path, ext=".xlsx"))

        return files

    def get_account_transactions(self) -> tuple[pl.DataFrame, Exception]:
        def _read_transactions_data_file(path: Path) -> pl.DataFrame:
            match path.suffix:
                case ".xlsx":
                    read_fn = lambda path: pl.read_excel(path)
                case ".csv":
                    read_fn = lambda path: pl.read_csv(path, truncate_ragged_lines=True)
                case _:
                    return path, None, ValueError(f"Unsupported file type: {path.suffix}")  
            try:
                df = read_fn(path)
                return path, df, None
            except Exception as e:
                return path, None, e

        paths = self.get_account_data_file_paths()

        transactions_dfs = [_read_transactions_data_file(path) for path in paths]

        if not transactions_dfs:
            return pl.DataFrame(), []

        all_transactions_df = pl.concat(
            [df for path, df, err in transactions_dfs if err is None]
        )

        errors = [(path, err) for path, _, err in transactions_dfs if err is not None]

        return all_transactions_df, errors


class SourceDataStore:
    deposit_account_data_stores: dict[str, DepositAccountDataStore]

    def __init__(self, data_config: DataConfig):
        self.data_config = data_config
        self.deposit_account_data_stores = {
            name: DepositAccountDataStore(
                deposit_account_data_config=deposit_account_config,
                entity_name=name,
            )
            for name, deposit_account_config in data_config.deposit_accounts.items()
        }


if __name__ == "__main__":
    load_env(EnvName.LIVE)

    data_root_dir = resolve_data_root_dir_from_env()
    data_config_path = resolve_config_dir_from_env()
    data_config_dict = load_config_dict_from_yaml(config_path=data_config_path)
    data_config = DataConfig.from_dict(data_root_dir=data_root_dir, data_config_dict=data_config_dict)

    barclays_deposit_accounts_data_store = DepositAccountDataStore(deposit_account_data_config=data_config.deposit_accounts['Barclays'], entity_name="Barclays")
    transactions, errors = barclays_deposit_accounts_data_store.get_account_transactions()

    print(transactions)

    source_data_store = SourceDataStore(data_config=data_config)
    print(source_data_store.deposit_account_data_stores)
