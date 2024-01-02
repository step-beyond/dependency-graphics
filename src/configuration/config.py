from dataclasses import dataclass


@dataclass
class Config:
    plain_config: any

    def get_directory(self) -> str:
        return self.plain_config.get("directory")

    def is_show_graph(self) -> bool:
        return self.plain_config.get("show-graph")

    def get_ignore_modules(self) -> [str]:
        if self.plain_config.get("ignore-modules") is None:
            return []
        return self.plain_config.get("ignore-modules")