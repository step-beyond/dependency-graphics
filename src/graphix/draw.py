from src.configuration.config import Config
from src.model.modules import ModuleGraph
from .draw_with_graphviz import draw


def draw_dependency_graph(module_graph: ModuleGraph, output_file_name: str, config: Config):
    draw(module_graph, output_file_name, config.get_draw_config())
