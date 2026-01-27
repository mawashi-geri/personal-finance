import argparse
from dataclasses import asdict
import json
from typing import Optional

from personal_finance.configuration.data_config import (
    DataConfig,
    EnvName,
    load_env,
    resolve_data_root_path_from_env,
)


def main(env_name: Optional[EnvName] = EnvName.DEV) -> None:
    if env_name:
        load_env(env_name=env_name)

    data_config = DataConfig.from_yaml(resolve_data_root_path_from_env())

    print(json.dumps(asdict(data_config), indent=4))


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument(
        "--env-name",
        default=EnvName.LIVE,
        type=EnvName,
    )
    args = arg_parser.parse_args()
    main(env_name=args.env_name)
