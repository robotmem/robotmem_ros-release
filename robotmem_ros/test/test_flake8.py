# Copyright 2026 gladego
#
# Licensed under the MIT License.

"""Flake8 code style check."""

import unittest

from ament_flake8.main import main_with_errors


class TestFlake8(unittest.TestCase):
    """Check Python code style with flake8."""

    def test_flake8(self):
        """Run ament_flake8 check."""
        rc, errors = main_with_errors(argv=[])
        self.assertEqual(
            rc, 0,
            'Found %d code style errors / warnings:\n' % len(errors)
            + '\n'.join(errors),
        )
