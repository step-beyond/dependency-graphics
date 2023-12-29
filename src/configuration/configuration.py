from dataclasses import dataclass

import yaml


@dataclass
class Configuration:
    plain_config: any

    def get_directory(self):
        return self.plain_config.get("directory")


configuration: Configuration
with open(".dependency-graphics-rc.yaml", "r", encoding="UTF-8") as stream:
    configuration = Configuration(yaml.safe_load(stream))


def get_configuration():
    return configuration
