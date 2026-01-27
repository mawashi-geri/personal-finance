from personal_finance.configuration.data_config import (
    DataConfig,
    resolve_data_root_path_from_env,
)


def test_data_config():
    data_config = DataConfig.from_yaml(resolve_data_root_path_from_env())

    print(data_config)

    assert data_config
