import pytest

from src.assertions.api_assertions import APIAssertions
from src.assertions.schema_assertions import SchemaAssertions
from src.schemas.auth_schema import LoginResponseSchema


@pytest.mark.regression
def test_login_with_valid_credentials(auth_client, payload_builder):
    payload = payload_builder.build_login_payload()
    response = auth_client.login(payload)

    APIAssertions.assert_status_code(response, 200)
    APIAssertions.assert_response_time_less_than(response, 5000)

    body = response.json()
    SchemaAssertions.validate_schema(LoginResponseSchema, body)