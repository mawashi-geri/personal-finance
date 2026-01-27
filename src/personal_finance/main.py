from personal_finance.configuration.data_config import (
    DataConfig,
    resolve_data_root_path_from_env,
)


def main():
    data_config = DataConfig.from_yaml(resolve_data_root_path_from_env())

    print(data_config)


if __name__ == "__main__":
    main()
