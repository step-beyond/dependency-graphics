import unittest

from assertpy import assert_that

from src.model.modules import ModuleGraph, Module
from src.transformation import transformation


class MyTestCase(unittest.TestCase):

    def test_does_ignore_modules(self):
        # GIVEN
        module_1: Module = Module("module_1", {"module_2"})
        module_2: Module = Module("module_2", {"module_1"})
        given: ModuleGraph = ModuleGraph([module_1, module_2])
        ignore_modules = ["module_2"]

        # WHEN
        result: ModuleGraph = transformation.ignore_modules(given, ignore_modules)

        # THEN
        assert_that(result.modules).is_length(1)
        assert_that(result.modules).contains(Module("module_1", set()))
        assert_that(result.modules).does_not_contain(Module("module_2", set()))

    def test_do_not_filter_due_to_no_matches(self):
        # GIVEN
        module_1: Module = Module("module_1", {"module_2"})
        module_2: Module = Module("module_2", {"module_1"})
        given: ModuleGraph = ModuleGraph([module_1, module_2])
        ignore_modules = ["module_3"]

        # WHEN
        result: ModuleGraph = transformation.ignore_modules(given, ignore_modules)

        # THEN
        assert_that(result.modules).is_length(2)
        assert_that(result.modules).contains(Module("module_1", {"module_2"}))
        assert_that(result.modules).contains(Module("module_2", {"module_1"}))

    def test_does_filter_all(self):
        # GIVEN
        module_1: Module = Module("module_1", ["module_2"])
        module_2: Module = Module("module_2", ["module_1"])
        given: ModuleGraph = ModuleGraph([module_1, module_2])
        ignore_modules = ["module_1", "module_2"]

        # WHEN
        result: ModuleGraph = transformation.ignore_modules(given, ignore_modules)

        # THEN
        assert_that(result.modules).is_empty()

    def test_aggregate_modules(self):
        # GIVEN
        module_1: Module = Module("module_1", {"module_2"})
        module_2: Module = Module("module_2", {"module_1", "module_2"})
        given: ModuleGraph = ModuleGraph([module_1, module_2])
        aggregate_modules = {"NEW_NAME": ["module_1", "module_2"]}

        # WHEN
        result: ModuleGraph = transformation.aggregate_modules(given, aggregate_modules)

        # THEN
        assert_that(result.modules).is_length(1)
        assert_that(result.modules).contains(Module("NEW_NAME", {"NEW_NAME"}))

    def test_aggregate_modules_and_dependencies(self):
        # GIVEN
        module_1: Module = Module("module_1", ["module_2"])
        module_2: Module = Module("module_2", ["module_1", "module_2"])
        module_3: Module = Module("module_3", ["module_1", "module_2"])
        given: ModuleGraph = ModuleGraph([module_1, module_2, module_3])
        aggregate_modules = {"NEW_NAME": ["module_1", "module_2"]}

        # WHEN
        result: ModuleGraph = transformation.aggregate_modules(given, aggregate_modules)

        # THEN
        assert_that(result.modules).is_length(2)
        assert_that(result.modules).contains(Module("NEW_NAME", {"NEW_NAME"}))
        assert_that(result.modules).contains(Module("module_3", {"NEW_NAME"}))

    def test_aggregate_nothing(self):
        # GIVEN
        module_1: Module = Module("module_1", ["module_2"])
        module_2: Module = Module("module_2", ["module_1", "module_2"])
        given: ModuleGraph = ModuleGraph([module_1, module_2])
        aggregate_modules = {"NEW_NAME": ["xxx", "bar"]}

        # WHEN
        result: ModuleGraph = transformation.aggregate_modules(given, aggregate_modules)

        # THEN
        assert_that(result.modules).is_length(2)
        assert_that(result.modules).contains(Module("module_1", {"module_2"}))
        assert_that(result.modules).contains(Module("module_2", {"module_1", "module_2"}))


if __name__ == '__main__':
    unittest.main()
