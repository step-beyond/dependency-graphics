from ..configuration.configuration import configuration
from ..model.modules import ModuleGraph
from ..parser import gradle_parser


def parse_module_tree() -> ModuleGraph:
    return gradle_parser.create_module_graph(configuration.get_directory())
