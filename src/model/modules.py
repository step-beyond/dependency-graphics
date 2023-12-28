from dataclasses import dataclass


@dataclass
class Module:
    name: str
    dependencies: [str]


@dataclass
class ModuleGraph:
    modules: [Module]
