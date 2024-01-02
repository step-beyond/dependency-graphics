import unittest
from unittest.mock import Mock

from assertpy import assert_that

from src.model.modules import ModuleGraph, Module
from src.transformation import transformation


class MyTestCase(unittest.TestCase):

    def test_does_ignore_modules(self):
        # GIVEN
        module_1: Module = Module("module_1", ["module_2"])
        module_2: Module = Module("module_2", ["module_1"])
        given: ModuleGraph = ModuleGraph([module_1, module_2])
        config = Mock()
        config.get_ignore_modules.return_value = ["module_2"]

        # WHEN
        result: ModuleGraph = transformation.transform_model(given, config)

        # THEN
        assert_that(result.modules).is_length(1)
        assert_that(result.modules).contains(Module("module_1", []))
        assert_that(result.modules).does_not_contain(Module("module_2", []))

    def test_do_not_filter_due_to_no_matches(self):
        # GIVEN
        module_1: Module = Module("module_1", ["module_2"])
        module_2: Module = Module("module_2", ["module_1"])
        given: ModuleGraph = ModuleGraph([module_1, module_2])
        config = Mock()
        config.get_ignore_modules.return_value = ["module_3"]

        # WHEN
        result: ModuleGraph = transformation.transform_model(given, config)

        # THEN
        assert_that(result.modules).is_length(2)
        assert_that(result.modules).contains(Module("module_1", ["module_2"]))
        assert_that(result.modules).contains(Module("module_2", ["module_1"]))


    def test_does_filter_all(self):
        # GIVEN
        module_1: Module = Module("module_1", ["module_2"])
        module_2: Module = Module("module_2", ["module_1"])
        given: ModuleGraph = ModuleGraph([module_1, module_2])
        config = Mock()
        config.get_ignore_modules.return_value = ["module_1", "module_2"]

        # WHEN
        result: ModuleGraph = transformation.transform_model(given, config)

        # THEN
        assert_that(result.modules).is_empty()


if __name__ == '__main__':
    unittest.main()
