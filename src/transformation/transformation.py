from src.configuration.config import Config
from src.model.modules import ModuleGraph, Module


def ignore_modules(model: ModuleGraph, ignored_modules: []) -> ModuleGraph:
    filtered_modules = []
    for module in model.modules:
        if module.name not in ignored_modules:
            filtered_modules.append(module)

    for filtered_module in filtered_modules:
        filtered_module.dependencies = {x for x in filtered_module.dependencies if
                                        x not in ignored_modules}
    return ModuleGraph(filtered_modules)


def aggregate_modules(model: ModuleGraph, aggregated_modules: {}):
    # aggregate modules
    for new_name, modules_to_aggregate in aggregated_modules.items():
        new_module = Module(new_name, set())
        something_to_aggregate: bool = False
        for module in model.modules:
            if module.name in modules_to_aggregate:
                something_to_aggregate = True
                new_module.dependencies.update(module.dependencies)
        if something_to_aggregate:
            model.modules.append(new_module)
            model.modules = [x for x in model.modules if x.name not in modules_to_aggregate]
    # replace with new module name
    for module in model.modules:
        new_module_dependencies = set(module.dependencies.copy())
        for new_name, modules_to_aggregate in aggregated_modules.items():
            for dependency in module.dependencies:
                if dependency in modules_to_aggregate:
                    new_module_dependencies.remove(dependency)
                    new_module_dependencies.add(new_name)
        module.dependencies = new_module_dependencies
    return model


def transform_model(model: ModuleGraph, config: Config) -> ModuleGraph:
    # transform modules
    model = ignore_modules(model, config.get_ignore_modules())
    model = aggregate_modules(model, config.get_aggregated_modules())
    return model
