from graphviz import Source

from src.configuration.config import Config
from src.model.modules import ModuleGraph


def draw(module_graph: ModuleGraph, config: Config):
    temp = """digraph G {
    edge [dir=forward]
    node [shape=plaintext]
"""
    for module in module_graph.modules:
        for dependency in module.dependencies:
            temp += "\t" \
                    + module.name.replace("-", "_") \
                    + " -> " \
                    + dependency.replace("-", "_") \
                    + "\n"

    temp += """}"""
    s = Source(temp, filename="out/test.gv", format="png")
    if config.is_show_graph():
        s.view()
