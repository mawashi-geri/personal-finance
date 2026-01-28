from pathlib import Path

import polars as pl
# import pandas as pd

from personal_finance.configuration.data_config import (
    DataConfig,
    load_env,
    EnvName,
    resolve_data_root_path_from_env,
)


class DepositAccountDataStore:
    def __init__(self, data_config: DataConfig):
        self.data_config = data_config

    def get_account_data_dir_paths(self) -> list[Path]:
        return [
            Path(self.data_config.root_path / account_config.root_dir / sub_dir)
            for account_config in self.data_config.deposit_accounts
            for sub_dir in account_config.sub_dirs
        ]

    def get_account_data_file_paths(self) -> list[Path]:
        data_dir_paths = self.get_account_data_dir_paths()

        def _find_files_in_directory(directory: Path) -> list[Path]:
            return [
                file for file in directory.expanduser().rglob("*.csv") if file.is_file()
            ]

        files = []
        for dir_path in data_dir_paths:
            files.extend(_find_files_in_directory(dir_path))

        return files

    def get_account_transactions(self) -> tuple[pl.DataFrame, Exception]:
        def _read_csv(path: Path) -> pl.DataFrame:
            try:
                df = pl.read_csv(path, truncate_ragged_lines=True)
                return path, df, None
            except Exception as e:
                return path, None, e

        transactions_dfs = [
            _read_csv(path) for path in self.get_account_data_file_paths()
        ]

        all_transactions_df = pl.concat([df for path, df, err in transactions_dfs if err is None])
        errors = [(path, err) for path, _, err in transactions_dfs if err is not None]

        return all_transactions_df, errors


if __name__ == "__main__":
    load_env(EnvName.LIVE)
    data_config = DataConfig.from_yaml(resolve_data_root_path_from_env())
    data_store = DepositAccountDataStore(data_config=data_config)
    transactions, errors = data_store.get_account_transactions()

    print(transactions)
