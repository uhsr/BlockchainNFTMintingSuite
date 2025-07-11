# test_blockchainnftmintingsuite.py
"""
Tests for BlockchainNFTMintingSuite module.
"""

import unittest
from blockchainnftmintingsuite import BlockchainNFTMintingSuite

class TestBlockchainNFTMintingSuite(unittest.TestCase):
    """Test cases for BlockchainNFTMintingSuite class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockchainNFTMintingSuite()
        self.assertIsInstance(instance, BlockchainNFTMintingSuite)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockchainNFTMintingSuite()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
