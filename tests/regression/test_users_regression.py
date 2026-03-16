import pytest

from src.assertions.api_assertions import APIAssertions
from src.utils.data_loader import DataLoader

users_data = DataLoader.load_json("data/users.json")


@pytest.mark.regression
@pytest.mark.parametrize("user_id", users_data["valid_user_ids"])
def test_get_single_user_by_valid_id(users_client, user_id):
    response = users_client.get_single_user(user_id)

    APIAssertions.assert_status_code(response, 200)
    APIAssertions.assert_response_time_less_than(response, 3000)

    body = response.json()
    APIAssertions.assert_contains_key_value(body, "id", user_id)
    APIAssertions.assert_type(body["firstName"], str, "firstName")
    APIAssertions.assert_type(body["lastName"], str, "lastName")
    APIAssertions.assert_type(body["email"], str, "email")


@pytest.mark.regression
@pytest.mark.parametrize("invalid_user_id", users_data["invalid_user_ids"])
def test_get_single_user_with_invalid_id(users_client, invalid_user_id):
    response = users_client.get_single_user(invalid_user_id)

    assert response.status_code in [400, 404, 500], (
        f"Unexpected status code for invalid user id {invalid_user_id}: "
        f"{response.status_code}. Response: {response.text}"
    )
