#!/usr/bin/env python3
"""
Test script for the Indian Address Matcher imports
"""

# Try different import approaches
print("Testing imports...")

try:
    # Import using package name
    from address_matcher.src.address_matcher import AddressMatcher
    print("SUCCESS: Imported AddressMatcher from address_matcher.src.address_matcher")
except ImportError as e:
    print(f"FAILED: {e}")

try:
    # Import from indian_address_matcher
    from indian_address_matcher.src.address_matcher import AddressMatcher
    print("SUCCESS: Imported AddressMatcher from indian_address_matcher.src.address_matcher")
except ImportError as e:
    print(f"FAILED: {e}")

try:
    # Import from root package
    from address_matcher import AddressMatcher
    print("SUCCESS: Imported AddressMatcher directly from address_matcher")
except ImportError as e:
    print(f"FAILED: {e}")

print("Test complete.") 