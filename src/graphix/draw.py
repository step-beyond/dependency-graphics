from src.model.modules import ModuleGraph
from .draw_with_graphviz import draw


def draw_dependency_graph(module_graph: ModuleGraph):
    draw(module_graph)
