import argparse
import os

from src.configuration import factory as config_factory
from src.configuration.config import Config
from src.transformation import transformation
from src.graphix import draw
from src.parser import parse


def execute(working_dir: str, config_file_path: str, output_file_name: str, code_path: str):
    configs: [Config] = config_factory.load_configs(working_dir, config_file_path)

    code_path = os.path.join(working_dir, code_path)
    module_tree = parse.parse_module_tree(code_path, configs[0])

    module_tree = transformation.transform_model(module_tree, configs)

    output_file_name = os.path.join(working_dir, output_file_name)
    draw.draw_dependency_graph(module_tree, output_file_name, configs[0])


def parse_args(plain_args: []):
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', default=".dependency-graphics-rc.yaml")
    parser.add_argument('-w', '--working-dir', required=True)
    parser.add_argument('-o', '--output', required=True)
    parser.add_argument('-a', '--analyze-code-path', required=True)
    parsed_args, _ = parser.parse_known_args(plain_args)
    return parsed_args


def run(args: []):
    args = parse_args(args)
    execute(args.working_dir, args.config, args.output, args.analyze_code_path)
