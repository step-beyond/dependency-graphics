from src.configuration import factory as config_factory
from src.configuration.config import Config
from src.transformation import transformation
from src.graphix import draw
from src.parser import parse


def main():
    config: Config = config_factory.load_config("./.dependency-graphics-rc.yaml")
    module_tree = parse.parse_module_tree(config)
    module_tree = transformation.transform_model(module_tree, config)
    draw.draw_dependency_graph(module_tree, config)


main()
