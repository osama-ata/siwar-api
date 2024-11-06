"""Constants used throughout the Siwar API wrapper."""

# API Base URL
API_BASE_URL = "https://api.siwar.ksaa.gov.sa"

# API Version
API_VERSION = "v1"

# Default timeout in seconds
DEFAULT_TIMEOUT = 30

# Default headers
DEFAULT_HEADERS = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

# Public API Endpoints
PUBLIC_ENDPOINTS = {
    'search': '/api/v1/external/public/search',
    'lexicons': '/api/v1/external/public/lexicons',
    'senses': '/api/v1/external/public/senses',
    'examples': '/api/v1/external/public/examples',
    'synonyms': '/api/v1/external/public/synonyms',
    'opposites': '/api/v1/external/public/opposites',
    'pos': '/api/v1/external/public/pos',
    'root': '/api/v1/external/public/root',
    'pattern': '/api/v1/external/public/pattern',
    'conjugations': '/api/v1/external/public/conjugations',
}

# Private API Endpoints (Not implemented yet)
PRIVATE_ENDPOINTS = {
    'search': '/api/v1/external/private/search',
    'senses': '/api/v1/external/private/senses',
    'examples': '/api/v1/external/private/examples',
    'synonyms': '/api/v1/external/private/synonyms',
    'opposites': '/api/v1/external/private/opposites',
    'pos': '/api/v1/external/private/pos',
    'root': '/api/v1/external/private/root',
    'pattern': '/api/v1/external/private/pattern',
    'conjugations': '/api/v1/external/private/conjugations',
}
