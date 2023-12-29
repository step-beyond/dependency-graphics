import os
import re
from typing import Optional

from ..model.modules import ModuleGraph, Module


def extract_dependency(line: str) -> Optional[str]:
    if " project(" in line and not line.startswith("//"):
        return re.sub(r"\'(\))*", "", line.split(":")[-1]).replace("\n", "").replace("\")", "")
    return None


def create_module_graph(directory: str) -> ModuleGraph:
    modules: [Module] = []
    for module_root, _, files in os.walk(directory):
        if "build.gradle" in files:
            module_name = module_root.split("/")[-1]
            with open(module_root + "/build.gradle", 'r', encoding="UTF-8") as file:
                module_dependencies = []
                for line in file.readlines():
                    module_dependency = extract_dependency(line)
                    if module_dependency is not None:
                        module_dependencies.append(module_dependency)
                modules.append(Module(module_name, module_dependencies))
    return ModuleGraph(modules)
