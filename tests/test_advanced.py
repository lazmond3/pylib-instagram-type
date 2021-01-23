# -*- coding: utf-8 -*-

from .context import use_hello

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(use_hello.hmm())


if __name__ == '__main__':
    unittest.main()
