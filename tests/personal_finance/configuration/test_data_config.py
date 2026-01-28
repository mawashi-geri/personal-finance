from dataclasses import asdict
import json

from personal_finance.configuration.data_config import (
    DataConfig,
    resolve_data_root_path_from_env,
)


def test_data_config():
    data_root_path = resolve_data_root_path_from_env()

    data_config = DataConfig.from_yaml(data_root_path=data_root_path)

    print(data_config)

    assert data_config
