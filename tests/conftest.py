from pathlib import Path
import os

import pytest

from personal_finance.configuration.data_config import (
    DataConfig,
    resolve_data_root_dir_from_env,
    resolve_config_dir_from_env,
    load_config_dict_from_yaml,
)


def load_test_env():
    env_vars = {
        "DATA_ROOT_DIR": str(Path(__file__).parent / "test_data"),
    }

    for key, value in env_vars.items():
        os.environ[key] = value


load_test_env()


@pytest.fixture(scope="session")
def data_root_dir():
    return resolve_data_root_dir_from_env()


@pytest.fixture(scope="session")
def data_config_dir():
    return resolve_config_dir_from_env()


@pytest.fixture(scope="session")
def data_config_dict():
    data_config_path = resolve_config_dir_from_env()
    return load_config_dict_from_yaml(config_path=data_config_path)


@pytest.fixture(scope="session")
def data_config(data_root_dir, data_config_dict):
    return DataConfig.from_dict(data_root_dir=data_root_dir, data_config_dict=data_config_dict)
