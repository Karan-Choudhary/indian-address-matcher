# Indian Address Matcher

A tool for determining whether two Indian addresses refer to the same location, even when they are written in different formats or with missing information.

## Features

- Preprocessing of Indian addresses
- Address similarity scoring using multiple algorithms
- Support for handling common variations in Indian address formats
- Configurable matching thresholds

## Installation

1. Clone this repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

```python
from src.address_matcher import AddressMatcher

# Initialize the matcher
matcher = AddressMatcher()

# Compare two addresses
address1 = "123, ABC Colony, Near XYZ Temple, Mumbai, Maharashtra - 400001"
address2 = "ABC Colony, 123, Mumbai, MH, 400001"

# Get matching score and result
score, is_match = matcher.match(address1, address2)
print(f"Match score: {score}")
print(f"Are addresses the same? {'Yes' if is_match else 'No'}")
```

## Methodology

The address matcher uses a combination of techniques:
1. Text normalization and standardization
2. Feature extraction from address components
3. Multiple similarity metrics (Levenshtein, Jaro-Winkler, TF-IDF, etc.)
4. Weighted scoring system for different address components

## Indian Address Specific Features

- Recognizes Indian state names and abbreviations
- Handles common variants of city/district names
- Processes pin codes and landmark references
- Accounts for typical Indian address patterns 