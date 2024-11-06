"""
Utility functions for the Siwar API wrapper.
"""

import re
from typing import List, Dict, Optional
from .constants import ARABIC_DIACRITICS

def strip_diacritics(text: str) -> str:
    """
    Remove Arabic diacritical marks from text.
    
    Args:
        text: Arabic text with diacritics
        
    Returns:
        Text without diacritics
    """
    return re.sub(f'[{ARABIC_DIACRITICS}]', '', text)

def validate_query(query: str) -> bool:
    """
    Validate search query string.
    
    Args:
        query: Query string to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    if not query or not isinstance(query, str):
        return False
    return bool(query.strip())

def validate_lexicon_ids(lexicon_ids: Optional[List[str]]) -> bool:
    """
    Validate lexicon IDs.
    
    Args:
        lexicon_ids: List of lexicon IDs to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    if lexicon_ids is None:
        return True
    if not isinstance(lexicon_ids, list):
        return False
    return all(isinstance(id_, str) and id_.strip() for id_ in lexicon_ids)

def build_query_params(
    query: str,
    lexicon_ids: Optional[List[str]] = None
) -> Dict[str, str]:
    """
    Build query parameters for API requests.
    
    Args:
        query: Search query
        lexicon_ids: Optional list of lexicon IDs
        
    Returns:
        Dictionary of query parameters
    """
    params = {'query': query}
    if lexicon_ids:
        params['lexiconIds'] = ','.join(lexicon_ids)
    return params

def format_error_message(error_code: str, details: Optional[str] = None) -> str:
    """
    Format error message with optional details.
    
    Args:
        error_code: Error code from constants.ERROR_MESSAGES
        details: Optional additional error details
        
    Returns:
        Formatted error message
    """
    from .constants import ERROR_MESSAGES
    message = ERROR_MESSAGES.get(error_code, 'Unknown error occurred')
    if details:
        message = f"{message} Details: {details}"
    return message

def is_valid_api_key(api_key: str) -> bool:
    """
    Validate API key format.
    
    Args:
        api_key: API key to validate
        
    Returns:
        bool: True if valid format, False otherwise
    """
    if not api_key or not isinstance(api_key, str):
        return False
    return bool(api_key.strip())
