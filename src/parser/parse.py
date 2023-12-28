from src.model.modules import ModuleGraph, Module


def parse_module_tree() -> ModuleGraph:
    module_list = [Module("Test", ["Test2"]), Module("Test2", [])]
    return ModuleGraph(module_list)
