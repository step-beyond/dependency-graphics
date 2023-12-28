from src.configuration import transformation
from src.graphix import draw
from src.parser import parse


def main():
    module_tree = parse.parse_module_tree()
    module_tree = transformation.transform_model(module_tree)
    draw.draw_dependency_graph(module_tree)


main()
