import unittest

from assertpy import assert_that

from src.model.modules import Module
from src.parser import gradle_parser


class MyTestCase(unittest.TestCase):

    def test_should_parse_internal_module_dependency(self):
        module_dependency = gradle_parser.extract_dependency("implementation project(':module_1')")
        assert_that(module_dependency).is_equal_to("module_1")

    def test_should_not_parse_external_module_dependency(self):
        module_dependency = gradle_parser\
            .extract_dependency("implementation 'org.springframework.boot:spring-boot-starter-web'")
        assert_that(module_dependency).is_equal_to(None)

    def test_should_not_parse_empty_dependency(self):
        module_dependency = gradle_parser.extract_dependency("")
        assert_that(module_dependency).is_equal_to(None)

    def test_does_parse_modules_correctly(self):
        directory: str = "./project"

        module_graph = gradle_parser.create_module_graph(directory)

        assert_that(module_graph.modules).is_length(3)
        assert_that(module_graph.modules).contains(Module("module_1", []))
        assert_that(module_graph.modules).contains(Module("module_2", ["module_1"]))
        assert_that(module_graph.modules).contains(Module("module_3", ["module_1", "module_2"]))


if __name__ == '__main__':
    unittest.main()
