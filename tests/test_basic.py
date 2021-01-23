# -*- coding: utf-8 -*-

# from .context import use_hello
import unittest
from . import context
use_hello = context.use_hello


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_absolute_truth_and_meaning(self):
        assert True


if __name__ == '__main__':
    unittest.main()
