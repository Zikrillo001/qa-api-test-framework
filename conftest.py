import os
import pytest
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture(scope="session")
def env_name():
    return os.getenv("ENV", "dev")


@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL", "https://dummyjson.com")