from src.configuration.config import Config
from src.model.modules import ModuleGraph


def remove_ignored_modules(model: ModuleGraph, config: Config) -> ModuleGraph:
    filtered_modules = []
    for module in model.modules:
        if module.name not in config.get_ignore_modules():
            filtered_modules.append(module)

    for filtered_module in filtered_modules:
        filtered_module.dependencies = [x for x in filtered_module.dependencies if
                                        x not in config.get_ignore_modules()]
    return ModuleGraph(filtered_modules)


def transform_model(model: ModuleGraph, config: Config) -> ModuleGraph:
    model = remove_ignored_modules(model, config)
    return model
