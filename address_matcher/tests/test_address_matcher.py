"""
Unit tests for the address matcher
"""
import unittest
import sys
import os

# Add the parent directory to sys.path to import the package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.address_matcher import AddressMatcher
from src.utils import preprocess_address, extract_address_components
from src.similarity import levenshtein_similarity, jaro_winkler_sim

class TestAddressMatcher(unittest.TestCase):
    """
    Test cases for the AddressMatcher class
    """
    
    def setUp(self):
        """
        Set up the test environment
        """
        self.matcher = AddressMatcher(threshold=0.75)
        
    def test_exact_address_match(self):
        """
        Test that identical addresses match
        """
        addr = "123, MG Road, Bangalore, Karnataka - 560001"
        score, is_match = self.matcher.match(addr, addr)
        self.assertEqual(score, 1.0)
        self.assertTrue(is_match)
        
    def test_different_formatting(self):
        """
        Test addresses with different formatting but same content
        """
        addr1 = "123, MG Road, Bangalore, Karnataka - 560001"
        addr2 = "123 MG Road Bangalore KA 560001"
        score, is_match = self.matcher.match(addr1, addr2)
        self.assertTrue(is_match)
        
    def test_abbreviated_state(self):
        """
        Test addresses with abbreviated state names
        """
        addr1 = "123, MG Road, Bangalore, Karnataka - 560001"
        addr2 = "123, MG Road, Bangalore, KA - 560001"
        score, is_match = self.matcher.match(addr1, addr2)
        self.assertTrue(is_match)
        
    def test_clearly_different_addresses(self):
        """
        Test clearly different addresses don't match
        """
        addr1 = "123, MG Road, Bangalore, Karnataka - 560001"
        addr2 = "456, Park Street, Kolkata, West Bengal - 700016"
        score, is_match = self.matcher.match(addr1, addr2)
        self.assertFalse(is_match)
        
    def test_preprocess_address(self):
        """
        Test address preprocessing
        """
        raw = "Flat No. 302, Tower C, Prestige Apts., Indira Nagar, Chennai - 600020"
        processed = preprocess_address(raw)
        self.assertIn("apartment", processed)
        self.assertIn("600020", processed)
        
    def test_pincode_extraction(self):
        """
        Test pincode extraction from address
        """
        addr = "123, MG Road, Bangalore, Karnataka - 560001"
        components = extract_address_components(preprocess_address(addr))
        self.assertEqual(components['pincode'], "560001")
        
    def test_levenshtein_similarity(self):
        """
        Test Levenshtein similarity function
        """
        text1 = "bangalore"
        text2 = "bengaluru"
        similarity = levenshtein_similarity(text1, text2)
        self.assertGreater(similarity, 0.5)
        
    def test_jaro_winkler_similarity(self):
        """
        Test Jaro-Winkler similarity function
        """
        text1 = "karnataka"
        text2 = "Karnataka"
        similarity = jaro_winkler_sim(text1, text2)
        self.assertGreater(similarity, 0.9)

if __name__ == '__main__':
    unittest.main() 