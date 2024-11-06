"""Core model definitions for the Siwar API wrapper."""

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional, Dict

from .enums import LemmaType, PartOfSpeech, ExampleType


@dataclass
class WordForm:
    """Word form representation."""
    form: str
    phonetic: Optional[str] = None
    dialect: Optional[str] = None
    audio: Optional[str] = None


@dataclass
class Translation:
    """Translation of a word."""
    word: str
    language: str
    language_label: str


@dataclass
class Example:
    """Example usage of a word."""
    word: str
    type: ExampleType
    source: Optional[str] = None
    audio: Optional[str] = None


@dataclass
class Sense:
    """Word sense/meaning."""
    definition: str
    translations: List[Translation] = field(default_factory=list)
    contexts: List[str] = field(default_factory=list)
    domains: List[str] = field(default_factory=list)
    examples: List[Example] = field(default_factory=list)
    relations: List[Dict[str, str]] = field(default_factory=list)
    image: Optional[str] = None


@dataclass
class SearchResult:
    """Search result from API."""
    # Required fields without defaults must come first
    lexical_entry_id: str
    lexicon_id: str
    lexicon_name: str
    lemma: str
    lemma_type: LemmaType
    pattern: str
    pos: PartOfSpeech
    non_diacritics_lemma: str
    lemma_language: str
    
    # Optional fields and fields with defaults follow
    lemma_audio: Optional[str] = None
    senses: List[Sense] = field(default_factory=list)
    root: List[str] = field(default_factory=list)
    word_forms: List[WordForm] = field(default_factory=list)
    is_word_form_match: bool = False
    is_dialect_match: bool = False
    is_lemmatizer: bool = False
    is_translation_match: bool = False
    is_synonym: bool = False
    sort_group_order: Optional[int] = None
    lexicon_search_order: Optional[int] = None


@dataclass
class LexiconEntry:
    """Lexicon entry."""
    # Required fields without defaults
    id: str
    name: str
    
    # Optional fields and fields with defaults
    title: Optional[str] = None
    version: Optional[str] = None
    version_date: Optional[str] = None
    is_published: bool = False
    publisher_name: Optional[str] = None
    description: Optional[str] = None
    domain_ids: List[str] = field(default_factory=list)
    status: str = "DRAFT"
    is_public: bool = False
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
