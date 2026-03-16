import requests

from src.utils.logger import get_logger


class BaseClient:
    def __init__(
        self, base_url: str, headers: dict | None = None, timeout: int = 10
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.headers = headers or {}
        self.timeout = timeout
        self.logger = get_logger(self.__class__.__name__)

    def _build_url(self, endpoint: str) -> str:
        return f"{self.base_url}/{endpoint.lstrip('/')}"

    def get(self, endpoint: str, params: dict | None = None) -> requests.Response:
        url = self._build_url(endpoint)
        self.logger.info(f"GET {url} | params={params}")
        response = requests.get(
            url,
            headers=self.headers,
            params=params,
            timeout=self.timeout,
        )
        self.logger.info(f"Response: {response.status_code}")
        return response

    def post(
        self,
        endpoint: str,
        json: dict | None = None,
        data: dict | None = None,
    ) -> requests.Response:
        url = self._build_url(endpoint)
        self.logger.info(f"POST {url} | json={json} | data={data}")
        response = requests.post(
            url,
            headers=self.headers,
            json=json,
            data=data,
            timeout=self.timeout,
        )
        self.logger.info(f"Response: {response.status_code}")
        return response

    def put(self, endpoint: str, json: dict | None = None) -> requests.Response:
        url = self._build_url(endpoint)
        self.logger.info(f"PUT {url} | json={json}")
        response = requests.put(
            url,
            headers=self.headers,
            json=json,
            timeout=self.timeout,
        )
        self.logger.info(f"Response: {response.status_code}")
        return response

    def patch(self, endpoint: str, json: dict | None = None) -> requests.Response:
        url = self._build_url(endpoint)
        self.logger.info(f"PATCH {url} | json={json}")
        response = requests.patch(
            url,
            headers=self.headers,
            json=json,
            timeout=self.timeout,
        )
        self.logger.info(f"Response: {response.status_code}")
        return response

    def delete(self, endpoint: str) -> requests.Response:
        url = self._build_url(endpoint)
        self.logger.info(f"DELETE {url}")
        response = requests.delete(
            url,
            headers=self.headers,
            timeout=self.timeout,
        )
        self.logger.info(f"Response: {response.status_code}")
        return response
