import os
from pathlib import Path

import yaml


class ConfigReader:
    def __init__(self) -> None:
        self.env = os.getenv("ENV", "dev")
        self.project_root = Path(__file__).resolve().parents[2]
        self.config_path = self.project_root / "config" / "environments" / f"{self.env}.yaml"
        self.config_data = self._load_config()

    def _load_config(self) -> dict:
        if not self.config_path.exists():
            raise FileNotFoundError(f"Config file not found: {self.config_path}")

        with open(self.config_path, "r", encoding="utf-8") as file:
            return yaml.safe_load(file)

    def get_base_url(self) -> str:
        return self.config_data["base_url"]

    def get_timeout(self) -> int:
        return self.config_data.get("timeout", 10)

    def get_headers(self) -> dict:
        return self.config_data.get("headers", {})