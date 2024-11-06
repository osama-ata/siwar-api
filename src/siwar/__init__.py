"""
Siwar API Python Wrapper
~~~~~~~~~~~~~~~~~~~~~~~

A Python wrapper for the Siwar Arabic Lexicon API.

Basic usage:
    >>> from siwar import SiwarClient
    >>> client = SiwarClient('your-api-key')
    >>> results = client.search_public('محرك')
"""

from .client import SiwarClient
from .exceptions import SiwarAPIError, SiwarAuthError
from .models import (
    LemmaType,
    PartOfSpeech,
    ExampleType,
    WordForm,
    Translation,
    Example,
    Sense,
    SearchResult,
    LexiconEntry,
)

__version__ = "0.1.0"
__author__ = "Osama Ata"
__license__ = "MIT"

__all__ = [
    "SiwarClient",
    "SiwarAPIError",
    "SiwarAuthError",
    "LemmaType",
    "PartOfSpeech",
    "ExampleType",
    "WordForm",
    "Translation",
    "Example",
    "Sense",
    "SearchResult",
    "LexiconEntry",
]
