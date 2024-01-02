from src.configuration.config import Config
from src.model.modules import ModuleGraph, Module


def ignore_modules(model: ModuleGraph, ignore_modules_list: []) -> ModuleGraph:
    filtered_modules = []
    for module in model.modules:
        if module.name not in ignore_modules_list:
            filtered_modules.append(module)

    for filtered_module in filtered_modules:
        filtered_module.dependencies = {x for x in filtered_module.dependencies if
                                        x not in ignore_modules_list}
    return ModuleGraph(filtered_modules)


def aggregate_modules(model: ModuleGraph, aggregate_modules_list: {}):
    # aggregate modules
    for new_name, modules_to_aggregate in aggregate_modules_list.items():
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
        for new_name, modules_to_aggregate in aggregate_modules_list.items():
            for dependency in module.dependencies:
                if dependency in modules_to_aggregate:
                    new_module_dependencies.remove(dependency)
                    new_module_dependencies.add(new_name)
        module.dependencies = new_module_dependencies
    return model


def ignore_dependencies(model: ModuleGraph, ignore_dependencies_list: []):
    for module in model.modules:
        for dependency in ignore_dependencies_list:
            from_dependency: str = dependency.split(":")[0]
            to_dependency: str = dependency.split(":")[1]
            if module.name == from_dependency:
                if to_dependency in module.dependencies:
                    module.dependencies.remove(to_dependency)
    return model


def transform_model(model: ModuleGraph, config: Config) -> ModuleGraph:
    # transform modules
    model = ignore_modules(model, config.get_ignore_modules())
    model = aggregate_modules(model, config.get_aggregated_modules())
    # transform dependencies
    model = ignore_dependencies(model, config.get_ignore_dependencies())
    return model
