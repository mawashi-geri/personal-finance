from pathlib import Path
import os


def load_test_env():
    env_vars = {
        "DATA_ROOT_PATH": str(Path(__file__).parent / "test_data"),
    }

    for key, value in env_vars.items():
        os.environ[key] = value


load_test_env()
