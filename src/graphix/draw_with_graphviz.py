from graphviz import Source

from src.model.modules import ModuleGraph
from src.configuration import configuration


def draw(module_graph: ModuleGraph):
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
    if configuration.get_configuration().is_show_graph():
        s.view()
