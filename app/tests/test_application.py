# -*- coding: utf-8 -*-
# pylint: disable=wrong-import-position
# pylint: disable=R0801
"""Test lambda_openai_v2 function."""

# python stuff
import os
import sys
import unittest
from pathlib import Path


HERE = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = str(Path(HERE).parent.parent)
PYTHON_ROOT = str(Path(PROJECT_ROOT).parent)
if PYTHON_ROOT not in sys.path:
    sys.path.append(PYTHON_ROOT)  # noqa: E402


from app.hello_world import hello_world  # noqa: E402


class TestApplication(unittest.TestCase):
    """Test Index Lambda function."""

    def test_application_does_not_crash(self):
        """Test that the application returns a value."""

        # pylint: disable=broad-exception-caught
        try:
            hello_world(language="Chinese")
        except Exception as e:
            self.fail(f"hello_world raised an exception: {e}")
