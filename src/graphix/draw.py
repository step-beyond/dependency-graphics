from src.configuration.config import Config
from src.model.modules import ModuleGraph
from .draw_with_graphviz import draw


def draw_dependency_graph(module_graph: ModuleGraph, config: Config):
    draw(module_graph, config.get_draw_config())
