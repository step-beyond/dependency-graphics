from graphviz import Source

from src.configuration.draw_config import DrawConfig
from src.model.modules import ModuleGraph


def draw(module_graph: ModuleGraph, output_file_name: str, config: DrawConfig):
    temp = """digraph G {
    edge [dir=forward]
    node [shape=box]
"""

    all_modules = {x.name for x in module_graph.modules}
    for module in module_graph.modules:
        all_modules.update(module.dependencies)

    for color_match in config.get_color_matching():
        module_prefix = color_match.split(":")[0]
        color = color_match.split(":")[1]
        for module in all_modules:
            if module.startswith(module_prefix):
                temp += "\t" + module.replace("-", "_") \
                        + " [style=filled,fillcolor=" + color + "]\n"

    for module in module_graph.modules:
        for dependency in module.dependencies:
            temp += "\t" \
                    + module.name.replace("-", "_") \
                    + " -> " \
                    + dependency.replace("-", "_") \
                    + "\n"

    temp += """}"""
    s = Source(temp, filename="out/" + output_file_name + ".gv", format="png")
    if config.is_show_graph():
        s.view()
