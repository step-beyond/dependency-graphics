import os
import yaml

from src.configuration.config import Config


def load_config(file_path: str) -> Config:
    with open(file_path, "r", encoding="UTF-8") as stream:
        return Config(yaml.safe_load(stream))


def load_configs(working_dir: str, file_name: str) -> [Config]:
    file_path: str = os.path.join(working_dir, file_name)
    config: Config = load_config(file_path)
    parent_configs: [Config] = []
    if config.get_parent_config() is not None:
        parent_configs += load_configs(working_dir, config.get_parent_config())
    parent_configs.append(config)
    return parent_configs
