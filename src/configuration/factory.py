import yaml

from src.configuration.config import Config


def load_config(file_path: str) -> Config:
    with open(file_path, "r", encoding="UTF-8") as stream:
        return Config(yaml.safe_load(stream))
