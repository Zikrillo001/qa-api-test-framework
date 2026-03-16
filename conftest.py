import pytest

from src.clients.auth_client import AuthClient
from src.clients.products_client import ProductsClient
from src.clients.users_client import UsersClient
from src.utils.config_reader import ConfigReader
from src.utils.payload_builder import PayloadBuilder


@pytest.fixture(scope="session")
def config():
    return ConfigReader()


@pytest.fixture(scope="session")
def base_url(config):
    return config.get_base_url()


@pytest.fixture(scope="session")
def headers(config):
    return config.get_headers()


@pytest.fixture(scope="session")
def timeout(config):
    return config.get_timeout()


@pytest.fixture(scope="session")
def products_client(base_url, headers, timeout):
    return ProductsClient(base_url=base_url, headers=headers, timeout=timeout)


@pytest.fixture(scope="session")
def users_client(base_url, headers, timeout):
    return UsersClient(base_url=base_url, headers=headers, timeout=timeout)


@pytest.fixture(scope="session")
def auth_client(base_url, headers, timeout):
    return AuthClient(base_url=base_url, headers=headers, timeout=timeout)


@pytest.fixture
def payload_builder():
    return PayloadBuilder()