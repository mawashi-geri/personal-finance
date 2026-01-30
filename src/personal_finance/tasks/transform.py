from typing import Optional

from personal_finance.configuration.data_config import (
    DataConfig,
    EnvName,
    load_config_dict_from_yaml,
    load_env,
    resolve_config_dir_from_env,
    resolve_data_root_dir_from_env,
)
from personal_finance.data_store.source.deposit_accounts import SourceDataStore
from personal_finance.transform.deposit_accounts.deposit_accounts import (
    transform_functions,
)


def transform_deposit_account_data(env_name: Optional[EnvName] = EnvName.LIVE) -> None:
    load_env(EnvName.LIVE)

    data_config_path = resolve_config_dir_from_env()
    data_root_dir = resolve_data_root_dir_from_env()
    data_config_dict = load_config_dict_from_yaml(config_path=data_config_path)
    data_config = DataConfig.from_dict(
        data_root_dir=data_root_dir, data_config_dict=data_config_dict
    )

    source_data_store = SourceDataStore(data_config=data_config)

    for (
        entity_name,
        deposit_account_data_store,
    ) in source_data_store.deposit_account_data_stores.items():
        transactions, errors = deposit_account_data_store.get_account_transactions()
        transformed_transactions = transform_functions[entity_name](transactions)
        print(f"Transformed transactions for entity {entity_name}:")
        print(transformed_transactions)


if __name__ == "__main__":
    transform_deposit_account_data()
