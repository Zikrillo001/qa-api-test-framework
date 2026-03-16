import pytest

from src.assertions.api_assertions import APIAssertions


@pytest.mark.smoke
def test_get_products_list(products_client):
    response = products_client.get_all_products()

    APIAssertions.assert_status_code(response, 200)
    APIAssertions.assert_response_time_less_than(response, 3000)

    body = response.json()
    APIAssertions.assert_json_has_key(body, "products")
    APIAssertions.assert_list_not_empty(body["products"])