import argparse
from dataclasses import asdict
import json
from typing import Optional

from personal_finance.configuration.data_config import (
    DataConfig,
    EnvName,
    load_env,
    resolve_data_root_dir_from_env,
    resolve_config_dir_from_env,
    load_config_dict_from_yaml,
)


def main(env_name: Optional[EnvName] = EnvName.DEV) -> None:
    if env_name:
        load_env(env_name=env_name)

    data_root_dir = resolve_data_root_dir_from_env()

    data_config_path = resolve_config_dir_from_env()

    data_config_dict = load_config_dict_from_yaml(config_path=data_config_path)

    data_config = DataConfig.from_dict(data_root_dir=data_root_dir, data_config_dict=data_config_dict)

    print(data_config)


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument(
        "--env-name",
        default=EnvName.LIVE,
        type=EnvName,
    )
    args = arg_parser.parse_args()
    main(env_name=args.env_name)
