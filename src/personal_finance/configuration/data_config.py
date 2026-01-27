from dataclasses import dataclass
import os
from pathlib import Path
from typing import Any
import yaml


def resolve_data_root_path_from_env():
    return os.environ["DATA_ROOT_PATH"]


@dataclass
class DepositAccountDataConfig:
    entity: str
    root_dir: str
    sub_dirs: list[str]

    @staticmethod
    def from_dict(d: dict[str, Any]):
        pass
        return DepositAccountDataConfig(
            entity=list(d.keys())[0],
            root_dir=d[list(d.keys())[0]]["root_dir"],
            sub_dirs=d[list(d.keys())[0]]["sub_dirs"],
        )


@dataclass
class DataConfig:
    data: list[DepositAccountDataConfig]

    @staticmethod
    def from_yaml(data_root_path: str = None):
        if data_root_path is None:
            data_root_path = resolve_data_root_path_from_env()

        data_root_path = data_root_path
        config_path = (
            Path(data_root_path).expanduser() / ".personal-finance/config.yaml"
        )

        config = yaml.safe_load(config_path.open("r"))

        return DataConfig(
            data=[
                DepositAccountDataConfig.from_dict(
                    {k: v}
                )
                for k, v in config["deposit_accounts"]["data"].items()
            ],
        )
