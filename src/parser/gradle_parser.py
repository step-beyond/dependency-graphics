import os
import re
from typing import Optional

from src.configuration.config import Config
from src.model.modules import ModuleGraph, Module


def extract_dependency(line: str, include_dep_re: str) -> Optional[str]:
    if line.startswith("//"):
        return None
    if " project(" in line:
        return re.sub(r"\'(\))*", "", line.split(":")[-1]).replace("\n", "").replace("\")", "")
    if ("implementation " in line or "api " in line) and \
        (include_dep_re != "" and re.match(r".*" + include_dep_re, line)):
        return line.split(":")[-1].replace("'", "")
    return None


def create_module_graph(directory: str, config: Config) -> ModuleGraph:
    modules: [Module] = []
    for module_root, _, files in os.walk(directory):
        if "build.gradle" in files:
            module_name = module_root.split("/")[-1]
            with open(module_root + "/build.gradle", 'r', encoding="UTF-8") as file:
                module_dependencies = set()
                for line in file.readlines():
                    module_dependency = extract_dependency(line, config.get_include_dependency_re())
                    if module_dependency is not None:
                        module_dependencies.add(module_dependency)
                modules.append(Module(module_name, module_dependencies))
    return ModuleGraph(modules)
