import unittest

from src import main


class MyTestCase(unittest.TestCase):

    def test_does_not_throw_any_exception(self):
        main.main()


if __name__ == '__main__':
    unittest.main()
