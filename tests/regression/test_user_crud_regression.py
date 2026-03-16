import pytest

from src.assertions.api_assertions import APIAssertions
from src.assertions.schema_assertions import SchemaAssertions
from src.schemas.user_schema import UserResponseSchema


@pytest.mark.regression
def test_create_user(users_client, payload_builder):
    payload = payload_builder.build_user_payload()
    response = users_client.create_user(payload)

    APIAssertions.assert_status_code(response, 201)

    body = response.json()
    APIAssertions.assert_json_has_key(body, "id")
    APIAssertions.assert_contains_key_value(body, "firstName", payload["firstName"])
    APIAssertions.assert_contains_key_value(body, "lastName", payload["lastName"])
    SchemaAssertions.validate_schema(UserResponseSchema, body)


@pytest.mark.regression
def test_update_user_with_put(users_client, payload_builder):
    payload = payload_builder.build_user_payload()
    response = users_client.update_user_put(1, payload)

    APIAssertions.assert_status_code(response, 200)

    body = response.json()
    APIAssertions.assert_contains_key_value(body, "id", 1)
    APIAssertions.assert_contains_key_value(body, "firstName", payload["firstName"])


@pytest.mark.regression
def test_update_user_with_patch(users_client, payload_builder):
    payload = payload_builder.build_partial_user_payload()
    response = users_client.update_user_patch(1, payload)

    APIAssertions.assert_status_code(response, 200)

    body = response.json()
    APIAssertions.assert_contains_key_value(body, "id", 1)
    APIAssertions.assert_contains_key_value(body, "firstName", payload["firstName"])


@pytest.mark.regression
def test_delete_user(users_client):
    response = users_client.delete_user(1)

    APIAssertions.assert_status_code(response, 200)

    body = response.json()
    APIAssertions.assert_contains_key_value(body, "id", 1)
    APIAssertions.assert_json_has_key(body, "isDeleted")