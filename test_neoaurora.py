# test_neoaurora.py
"""
Tests for NeoAurora module.
"""

import unittest
from neoaurora import NeoAurora

class TestNeoAurora(unittest.TestCase):
    """Test cases for NeoAurora class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NeoAurora()
        self.assertIsInstance(instance, NeoAurora)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NeoAurora()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
