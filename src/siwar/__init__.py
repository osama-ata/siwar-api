"""Siwar API Python Wrapper"""

from .client import SiwarClient
from .exceptions import SiwarAPIError, SiwarAuthError
from .models.core import SearchResult, LexiconEntry, WordForm, Translation, Example, Sense
from .models.enums import LemmaType, PartOfSpeech, ExampleType

__version__ = "0.1.0"

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
