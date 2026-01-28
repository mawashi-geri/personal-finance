from personal_finance import DepositAccountDataStore, DataConfig, load_env, EnvName, resolve_data_root_path_from_env


def test_deposit_account_data_store():
    load_env(EnvName.LIVE)
    data_config = DataConfig.from_yaml(resolve_data_root_path_from_env())
    data_store = DepositAccountDataStore(data_config=data_config)
    transactions, errors = data_store.get_account_transactions()

    print(transactions)