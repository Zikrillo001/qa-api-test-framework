import requests
import pytest


@pytest.mark.smoke
def test_get_products_list(base_url):
    response = requests.get(f"{base_url}/products", timeout=10)

    assert response.status_code == 200
    body = response.json()

    assert "products" in body
    assert isinstance(body["products"], list)
    assert len(body["products"]) > 0