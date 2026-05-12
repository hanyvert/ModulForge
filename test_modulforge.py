# test_modulforge.py
"""
Tests for ModulForge module.
"""

import unittest
from modulforge import ModulForge

class TestModulForge(unittest.TestCase):
    """Test cases for ModulForge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ModulForge()
        self.assertIsInstance(instance, ModulForge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ModulForge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
