import pytest
import sys
import os

def test_basic():
    """Basic test to ensure testing works"""
    assert True

def test_import():
    """Test that basic imports work"""
    assert 'pytest' in sys.modules

def test_workspace_access():
    """Ensure we can access workspace"""
    assert os.path.exists('/workspace')
