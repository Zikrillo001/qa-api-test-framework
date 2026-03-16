import pytest

from src.assertions.api_assertions import APIAssertions


@pytest.mark.integration
def test_user_lifecycle_flow(users_client, payload_builder):
    create_payload = payload_builder.build_user_payload()

    create_response = users_client.create_user(create_payload)
    APIAssertions.assert_status_code(create_response, 201)

    created_body = create_response.json()
    APIAssertions.assert_json_has_key(created_body, "id")
    APIAssertions.assert_contains_key_value(
        created_body, "firstName", create_payload["firstName"]
    )
    APIAssertions.assert_contains_key_value(
        created_body, "lastName", create_payload["lastName"]
    )

    existing_user_id = 1

    patch_payload = payload_builder.build_partial_user_payload()
    patch_response = users_client.update_user_patch(existing_user_id, patch_payload)
    APIAssertions.assert_status_code(patch_response, 200)

    patched_body = patch_response.json()
    APIAssertions.assert_contains_key_value(patched_body, "id", existing_user_id)
    APIAssertions.assert_contains_key_value(
        patched_body, "firstName", patch_payload["firstName"]
    )

    delete_response = users_client.delete_user(existing_user_id)
    APIAssertions.assert_status_code(delete_response, 200)

    deleted_body = delete_response.json()
    APIAssertions.assert_contains_key_value(deleted_body, "id", existing_user_id)
