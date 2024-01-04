import os
import unittest

from assertpy import assert_that

from src.configuration.config import Config
from src.model.modules import Module
from src.parser import gradle_parser


class MyTestCase(unittest.TestCase):

    def test_should_parse_internal_module_dependency(self):
        module_dependency = gradle_parser.extract_dependency("implementation project(':module_1')",
                                                             "")
        assert_that(module_dependency).is_equal_to("module_1")

    def test_should_not_parse_external_module_dependency(self):
        module_dependency = gradle_parser \
            .extract_dependency("implementation 'org.springframework.boot:spring-boot-starter-web'",
                                "")
        assert_that(module_dependency).is_equal_to(None)

    def test_should_not_parse_empty_dependency(self):
        module_dependency = gradle_parser.extract_dependency("", "")
        assert_that(module_dependency).is_equal_to(None)

    def test_should_not_parse_any_project(self):
        module_dependency = gradle_parser.extract_dependency \
            ("property 'sonar.coverage.jacoco.xmlReportPaths', '${project.rootDir}/application/'",
             "")
        assert_that(module_dependency).is_equal_to(None)

    def test_should_parse_implementation_project(self):
        module_dependency = gradle_parser.extract_dependency \
            ("implementation 'com.my.special.library:my-special-library'", "com.my.special.")
        assert_that(module_dependency).is_equal_to("my-special-library")

    def test_should_parse_test_implementation_project(self):
        module_dependency = gradle_parser.extract_dependency \
            ("testImplementation 'com.my.special.library:my-special-library'", "")
        assert_that(module_dependency).is_equal_to(None)

    def test_should_parse_api_project(self):
        module_dependency = gradle_parser.extract_dependency \
            ("api 'com.my.special.library:my-special-library'", "my-special-library")
        assert_that(module_dependency).is_equal_to("my-special-library")

    def test_does_parse_modules_correctly(self):
        this_dir = os.path.dirname(os.path.abspath(__file__))
        directory: str = os.path.join(this_dir, "../resources/example_project/")
        config: Config = Config({"include-dependency-re": ""})

        module_graph = gradle_parser.create_module_graph(directory, config)

        assert_that(module_graph.modules).is_length(3)
        assert_that(module_graph.modules).contains(Module("module_1", set()))
        assert_that(module_graph.modules).contains(Module("module_2", {"module_1"}))
        assert_that(module_graph.modules).contains(Module("module_3", {"module_1", "module_2"}))


if __name__ == '__main__':
    unittest.main()
