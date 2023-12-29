from dataclasses import dataclass

import yaml


@dataclass
class Configuration:
    plain_config: any

    def get_directory(self) -> str:
        return self.plain_config.get("directory")

    def is_show_graph(self) -> bool:
        return self.plain_config.get("show-graph")


def load_config(path: str) -> Configuration:
    with open(path, "r", encoding="UTF-8") as stream:
        return Configuration(yaml.safe_load(stream))


configuration: Configuration = load_config(".dependency-graphics-rc.yaml")


def get_configuration():
    return configuration
