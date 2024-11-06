"""
Constants used throughout the Siwar API wrapper.
"""

# API Base URL
API_BASE_URL = "https://api.siwar.ksaa.gov.sa"

# API Version
API_VERSION = "v1"

# API Endpoints
ENDPOINTS = {
    'public_search': '/api/v1/external/public/search',
    'private_search': '/api/v1/external/private/search',
    'public_lexicons': '/api/v1/external/public/lexicons',
    'public_senses': '/api/v1/external/public/senses',
    'private_senses': '/api/v1/external/private/senses',
    'public_examples': '/api/v1/external/public/examples',
    'private_examples': '/api/v1/external/private/examples',
    'public_synonyms': '/api/v1/external/public/synonyms',
    'private_synonyms': '/api/v1/external/private/synonyms',
    'public_opposites': '/api/v1/external/public/opposites',
    'private_opposites': '/api/v1/external/private/opposites',
    'public_pos': '/api/v1/external/public/pos',
    'private_pos': '/api/v1/external/private/pos',
    'public_root': '/api/v1/external/public/root',
    'private_root': '/api/v1/external/private/root',
    'public_pattern': '/api/v1/external/public/pattern',
    'private_pattern': '/api/v1/external/private/pattern',
    'public_conjugations': '/api/v1/external/public/conjugations',
    'private_conjugations': '/api/v1/external/private/conjugations',
}

# HTTP Methods
GET = 'GET'
POST = 'POST'

# Default timeout in seconds
DEFAULT_TIMEOUT = 30

# Default headers
DEFAULT_HEADERS = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

# Error Messages
ERROR_MESSAGES = {
    'auth_error': 'Authentication failed. Please check your API key.',
    'invalid_params': 'Invalid parameters provided.',
    'network_error': 'Network error occurred.',
    'timeout_error': 'Request timed out.',
    'rate_limit': 'API rate limit exceeded.',
    'server_error': 'Server error occurred.',
    'parse_error': 'Failed to parse API response.',
}

# Arabic Diacritics
ARABIC_DIACRITICS = '\u064B\u064C\u064D\u064E\u064F\u0650\u0651\u0652\u0670'
