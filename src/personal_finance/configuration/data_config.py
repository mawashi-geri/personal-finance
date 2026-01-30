from dataclasses import asdict, dataclass
from enum import StrEnum
import json
import os
from pathlib import Path
from typing import Any, Optional
import yaml

from dotenv import load_dotenv


from personal_finance.configuration.log_config import get_logger
from personal_finance.utils.utils import StrMixin


logger = get_logger(name=__name__)


DATA_ROOT_DIR: str = "DATA_ROOT_DIR"

LIVE: str = "live"
DEV: str = "dev"
TEST: str = "test"


class EnvName(StrEnum):
    LIVE = "live"
    DEV = "dev"
    TEST = "test"


def load_env(env_name: EnvName) -> None:
    env_file_path = (
        Path(__file__).parent / 
        ".." / ".." / ".." / "env_files" /
        f".env.{env_name.value}"
    )

    logger.info(f"Loading environment variables from: {env_file_path.resolve()}")

    load_dotenv(dotenv_path=env_file_path)


def resolve_data_root_dir_from_env() -> Path:
    data_root_path = Path(os.environ[DATA_ROOT_DIR]).expanduser()

    return data_root_path

def resolve_config_dir_from_env() -> Path:
    config_path = Path(resolve_data_root_dir_from_env()) / '.personal-finance/config.yaml'

    return config_path


def load_config_dict_from_yaml(config_path: Optional[Path] = None) -> dict[str, Any]:
    if not config_path:
        config_path = resolve_config_dir_from_env()

    config_dict = yaml.safe_load(config_path.open("r"))

    return config_dict


@dataclass
class DepositAccountDataConfig(StrMixin):
    root_dir: str
    entity_name: str
    entity_dir: str
    sub_dirs: list[str]

    @staticmethod
    def from_dict(root_dir: str, entity_name: str, d: dict[str, Any]):
        return DepositAccountDataConfig(
            root_dir=str(root_dir),
            entity_name=entity_name,
            entity_dir=d['entity_dir'],
            sub_dirs=d["sub_dirs"],
        )


@dataclass
class DataConfig(StrMixin):
    root_dir: str
    deposit_accounts: dict[str, DepositAccountDataConfig]

    @staticmethod
    def from_dict(data_root_dir: str, data_config_dict: dict[str, Any]):
        return DataConfig(
            root_dir=str(data_root_dir),
            deposit_accounts={
                k: DepositAccountDataConfig.from_dict(root_dir=data_root_dir, entity_name=k, d=v)
                for k, v in data_config_dict["deposit_accounts"]["data"].items()
            },
        )


if __name__ == "__main__":
    load_env(EnvName.LIVE)
    data_config = DataConfig.from_dict(data_root_dir=resolve_data_root_dir_from_env(), data_config_dict=load_config_dict_from_yaml())
    print(data_config)

    for deposit_account_config in data_config.deposit_accounts.values():
        print(deposit_account_config)
