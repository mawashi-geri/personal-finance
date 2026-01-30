import pytest

from personal_finance import SourceDepositAccountDataStore, DataConfig, load_env, EnvName, resolve_data_root_dir_from_env
from personal_finance.configuration.data_config import load_config_dict_from_yaml, resolve_config_dir_from_env


@pytest.mark.parametrize("entity_name", ["Barclays", "Skipton"])
def test_source_deposit_account_data_store(entity_name, data_config: DataConfig) -> None:
    data_store = SourceDepositAccountDataStore(deposit_account_data_config=data_config.deposit_accounts[entity_name], entity_name=entity_name)
    transactions, errors = data_store.get_account_transactions()

    print(transactions)
    assert not errors


def test_source_deposit_account_data_stores(data_config: DataConfig) -> None:
    from personal_finance.data_store.source.deposit_accounts import SourceDataStore

    source_data_store = SourceDataStore(data_config=data_config)

    for entity_name, deposit_account_data_store in source_data_store.deposit_account_data_stores.items():
        transactions, errors = deposit_account_data_store.get_account_transactions()
        print(f"Entity: {entity_name}")
        print(transactions)
        assert not errors


if __name__ == "__main__":
    load_env(EnvName.TEST)

    data_root_dir = resolve_data_root_dir_from_env()
    data_config_path = resolve_config_dir_from_env()
    data_config_dict = load_config_dict_from_yaml(config_path=data_config_path)
    data_config = DataConfig.from_dict(data_root_dir=data_root_dir, data_config_dict=data_config_dict)

    test_source_deposit_account_data_store(data_config=data_config)