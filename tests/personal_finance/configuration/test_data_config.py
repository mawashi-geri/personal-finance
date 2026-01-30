from personal_finance.configuration.data_config import (
    DataConfig,
    DepositAccountDataConfig,
)


def test_deposit_account_data_config():
    expected = DepositAccountDataConfig(
        root_dir="root_dir",
        entity_name="TestAccount",
        entity_dir="entity_dir",
        sub_dirs=["subdir1", "subdir2"],
    )

    actual = DepositAccountDataConfig.from_dict(
        root_dir="root_dir",
        entity_name="TestAccount",
        d={
            "entity_dir": "entity_dir",
            "sub_dirs": ["subdir1", "subdir2"],
        },
    )

    assert actual == expected


def test_data_config(data_root_dir, data_config_dict):

    data_config = DataConfig.from_dict(data_root_dir=data_root_dir, data_config_dict=data_config_dict)
    print(data_config)

    assert data_config
