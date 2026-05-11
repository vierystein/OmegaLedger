# test_omegaledger.py
"""
Tests for OmegaLedger module.
"""

import unittest
from omegaledger import OmegaLedger

class TestOmegaLedger(unittest.TestCase):
    """Test cases for OmegaLedger class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = OmegaLedger()
        self.assertIsInstance(instance, OmegaLedger)
        
    def test_run_method(self):
        """Test the run method."""
        instance = OmegaLedger()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
