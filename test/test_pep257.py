# Copyright 2026 gladego
#
# Licensed under the MIT License.

"""PEP 257 docstring check."""

import unittest

from ament_pep257.main import main


class TestPep257(unittest.TestCase):
    """Check docstring conventions with pep257."""

    def test_pep257(self):
        """Run ament_pep257 check."""
        rc = main(argv=['.', 'test'])
        self.assertEqual(rc, 0, 'Found code style errors / warnings')
