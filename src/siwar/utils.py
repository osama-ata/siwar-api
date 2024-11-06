"""Utility functions for Siwar API."""

from typing import Dict, List, Optional, cast
import re
import json

from .constants import ARABIC_DIACRITICS, ERROR_MESSAGES

def strip_diacritics(text: str) -> str:
    """
    Remove Arabic diacritical marks from text.
    
    Args:
        text: Arabic text with diacritics
            
    Returns:
        Text without diacritics
    """
    # Arabic diacritics regex pattern
    diacritics = re.compile(f'[{ARABIC_DIACRITICS}]')
    return diacritics.sub('', text)

def format_error_message(error_type: str, details: Optional[str] = None) -> str:
    """
    Format error message with optional details.
    
    Args:
        error_type: Type of error from ERROR_MESSAGES
        details: Additional error details
            
    Returns:
        Formatted error message
    """
    message = ERROR_MESSAGES.get(error_type, 'An unknown error occurred')
    if details:
        message = f"{message} Details: {details}"
    return message

def format_lexicon_ids(lexicon_ids: Optional[List[str]]) -> Optional[str]:
    """
    Format lexicon IDs for API requests.
    
    Args:
        lexicon_ids: List of lexicon IDs
            
    Returns:
        Comma-separated string of lexicon IDs or None
    """
    if not lexicon_ids:
        return None
    return ','.join(lexicon_ids)

def parse_response(response_text: str, error_on_empty: bool = True) -> Dict:
    """
    Parse JSON response text.
    
    Args:
        response_text: JSON response string
        error_on_empty: Whether to raise error for empty response
            
    Returns:
        Parsed JSON data
    """
    try:
        data = json.loads(response_text)
        if error_on_empty and not data:
            raise ValueError(format_error_message('parse_error', 'Empty response'))
        return cast(Dict, data)
    except json.JSONDecodeError as e:
        raise ValueError(format_error_message('parse_error', str(e)))

def validate_api_key(api_key: str) -> None:
    """
    Validate API key format.
    
    Args:
        api_key: API key to validate
            
    Raises:
        ValueError: If API key is invalid
    """
    if not api_key or not isinstance(api_key, str):
        raise ValueError(format_error_message('auth_error', 'Invalid API key format'))
