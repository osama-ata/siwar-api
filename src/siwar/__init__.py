"""
Siwar API Python Wrapper
~~~~~~~~~~~~~~~~~~~~~~~

A Python wrapper for the Siwar Arabic Lexicon API.

Basic usage:
    >>> from siwar import SiwarClient
    >>> client = SiwarClient('your-api-key')
    >>> results = client.search_public('محرك')

:copyright: (c) 2024 by Osama Ata.
:license: MIT, see LICENSE for more details.
"""

from .client import SiwarClient
from .exceptions import SiwarAPIError, SiwarAuthError
from .models import (
    LemmaType,
    PartOfSpeech,
    ExampleType,
    SearchResult,
    LexiconEntry,
    WordForm
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
    "SearchResult",
    "LexiconEntry",
    "WordForm",
]
