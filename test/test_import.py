# Copyright 2026 gladego
#
# Licensed under the MIT License.

"""Basic import test for robotmem_ros."""

import unittest


class TestImport(unittest.TestCase):
    """Verify robotmem_ros package is importable."""

    def test_import_robotmem_ros(self):
        """Import robotmem_ros successfully."""
        import robotmem_ros  # noqa: F401
        self.assertIsNotNone(robotmem_ros)
