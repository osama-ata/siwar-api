"""Test configuration and shared utilities for Siwar API tests."""

import os
from pathlib import Path

# Test data directory for fixture files
TEST_DATA_DIR = Path(__file__).parent / "data"

# Constants used across tests
TEST_API_KEY = "test_api_key"
TEST_BASE_URL = "https://api.siwar.ksaa.gov.sa"

# Sample test data
SAMPLE_WORD = "محرك"
SAMPLE_LEXICON_ID = "123"

# Create test data directory if it doesn't exist
TEST_DATA_DIR.mkdir(exist_ok=True)

# Define helper functions that might be used across multiple test files
def get_fixture_path(filename: str) -> Path:
    """Get the full path to a test fixture file."""
    return TEST_DATA_DIR / filename

def load_fixture(filename: str) -> str:
    """Load a test fixture file."""
    with open(get_fixture_path(filename), "r", encoding="utf-8") as f:
        return f.read()
