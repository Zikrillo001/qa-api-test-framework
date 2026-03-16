class APIAssertions:
    @staticmethod
    def assert_status_code(response, expected_status: int) -> None:
        actual_status = response.status_code
        assert actual_status == expected_status, (
            f"Expected status code {expected_status}, but got {actual_status}. "
            f"Response body: {response.text}"
        )

    @staticmethod
    def assert_response_time_less_than(response, max_ms: int) -> None:
        actual_ms = int(response.elapsed.total_seconds() * 1000)
        assert actual_ms < max_ms, (
            f"Expected response time < {max_ms} ms, but got {actual_ms} ms"
        )

    @staticmethod
    def assert_json_has_key(json_data: dict, key: str) -> None:
        assert key in json_data, f"Expected key '{key}' not found in response: {json_data}"

    @staticmethod
    def assert_list_not_empty(items: list) -> None:
        assert isinstance(items, list), f"Expected list, but got {type(items).__name__}"
        assert len(items) > 0, "Expected non-empty list, but list is empty"