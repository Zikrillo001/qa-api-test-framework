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
        assert (
            actual_ms < max_ms
        ), f"Expected response time < {max_ms} ms, but got {actual_ms} ms"

    @staticmethod
    def assert_json_has_key(json_data: dict, key: str) -> None:
        assert (
            key in json_data
        ), f"Expected key '{key}' not found in response: {json_data}"

    @staticmethod
    def assert_list_not_empty(items: list) -> None:
        assert isinstance(items, list), f"Expected list, but got {type(items).__name__}"
        assert len(items) > 0, "Expected non-empty list, but list is empty"

    @staticmethod
    def assert_equal(actual, expected, field_name: str = "value") -> None:
        assert (
            actual == expected
        ), f"Expected {field_name} to be {expected}, but got {actual}"

    @staticmethod
    def assert_type(value, expected_type, field_name: str = "value") -> None:
        if isinstance(expected_type, tuple):
            expected_names = ", ".join(t.__name__ for t in expected_type)
            assert isinstance(value, expected_type), (
                f"Expected {field_name} to be one of ({expected_names}), "
                f"but got {type(value).__name__}"
            )
        else:
            assert isinstance(value, expected_type), (
                f"Expected {field_name} to be of type {expected_type.__name__}, "
                f"but got {type(value).__name__}"
            )

    @staticmethod
    def assert_greater_than(actual, threshold, field_name: str = "value") -> None:
        assert (
            actual > threshold
        ), f"Expected {field_name} to be > {threshold}, but got {actual}"

    @staticmethod
    def assert_contains_key_value(json_data: dict, key: str, expected_value) -> None:
        assert (
            key in json_data
        ), f"Expected key '{key}' not found in response: {json_data}"
        assert (
            json_data[key] == expected_value
        ), f"Expected '{key}' to be '{expected_value}', but got '{json_data[key]}'"
