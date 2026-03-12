# Copyright 2026 gladego
#
# Licensed under the MIT License.

"""Copyright notice check."""

import unittest

from ament_copyright.main import main


class TestCopyright(unittest.TestCase):
    """Check all files have copyright notice."""

    def test_copyright(self):
        """Run ament_copyright check."""
        rc = main(argv=['.', 'test'])
        self.assertEqual(rc, 0, 'Found copyright errors')
