import pytest

from src.assertions.api_assertions import APIAssertions
from src.utils.data_loader import DataLoader

products_data = DataLoader.load_json("data/products.json")


@pytest.mark.regression
@pytest.mark.parametrize("product_id", products_data["valid_product_ids"])
def test_get_single_product_by_valid_id(products_client, product_id):
    response = products_client.get_single_product(product_id)

    APIAssertions.assert_status_code(response, 200)
    APIAssertions.assert_response_time_less_than(response, 3000)

    body = response.json()
    APIAssertions.assert_contains_key_value(body, "id", product_id)
    APIAssertions.assert_type(body["title"], str, "title")
    APIAssertions.assert_type(body["price"], int, "price")


@pytest.mark.regression
@pytest.mark.parametrize("query", products_data["search_queries"])
def test_search_products_with_valid_query(products_client, query):
    response = products_client.search_products(query)

    APIAssertions.assert_status_code(response, 200)
    APIAssertions.assert_response_time_less_than(response, 3000)

    body = response.json()
    APIAssertions.assert_json_has_key(body, "products")
    APIAssertions.assert_type(body["products"], list, "products")


@pytest.mark.regression
@pytest.mark.parametrize("query", products_data["empty_like_queries"])
def test_search_products_with_no_matching_query(products_client, query):
    response = products_client.search_products(query)

    APIAssertions.assert_status_code(response, 200)

    body = response.json()
    APIAssertions.assert_json_has_key(body, "products")
    APIAssertions.assert_type(body["products"], list, "products")
    APIAssertions.assert_equal(len(body["products"]), 0, "products count")


@pytest.mark.regression
@pytest.mark.parametrize("invalid_product_id", products_data["invalid_product_ids"])
def test_get_single_product_with_invalid_id(products_client, invalid_product_id):
    response = products_client.get_single_product(invalid_product_id)

    assert response.status_code in [400, 404, 500], (
        f"Unexpected status code for invalid product id {invalid_product_id}: "
        f"{response.status_code}. Response: {response.text}"
    )