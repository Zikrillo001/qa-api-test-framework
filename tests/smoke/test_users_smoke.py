import pytest

from src.assertions.api_assertions import APIAssertions


@pytest.mark.smoke
def test_get_users_list(users_client):
    response = users_client.get_all_users()

    APIAssertions.assert_status_code(response, 200)
    APIAssertions.assert_response_time_less_than(response, 3000)

    body = response.json()
    APIAssertions.assert_json_has_key(body, "users")
    APIAssertions.assert_list_not_empty(body["users"])