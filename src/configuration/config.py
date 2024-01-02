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

    def get_aggregated_modules(self) -> {}:
        if self.plain_config.get("aggregate-modules") is None:
            return {}
        return self.plain_config.get("aggregate-modules")

    def get_ignore_dependencies(self) -> []:
        if self.plain_config.get("ignore-dependencies") is None:
            return {}
        return self.plain_config.get("ignore-dependencies")

    def get_add_dependencies(self) -> []:
        if self.plain_config.get("add-dependencies") is None:
            return {}
        return self.plain_config.get("add-dependencies")

    def get_add_modules(self) -> []:
        if self.plain_config.get("add-modules") is None:
            return {}
        return self.plain_config.get("add-modules")
