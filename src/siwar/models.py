"""Models for the Siwar API wrapper."""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import List, Optional, Dict, Any

class LemmaType(str, Enum):
    """Types of lemmas in Arabic lexicon."""
    SINGLE_WORD = "singleWord"  # مفردة
    MWE = "MWE"  # مركب اسمي
    WASF = "wasf"  # مركب وصفي
    THRF = "thrf"  # مركب ظرفي
    PHRASE_VERB = "phraseVerb"  # مركب فعلي
    COMPOUND = "compound"  # مركب حرفي
    MORPHIM = "morphim"  # مورفيم مقيد
    SYMBOL = "symbol"  # رمز
    SHORT = "short"  # اختصار
    MARK = "mark"  # علامة ترقيم
    SGN_COM = "SgnCom"  # مركب إشاري
    MSL_COM = "MslCom"  # مركب موصولي
    PRO_COM = "ProCom"  # مركب ضميري
    INFC = "infc"  # مركب انفعالي
    NMBR = "nmbr"  # رقم

class PartOfSpeech(str, Enum):
    """Parts of speech in Arabic."""
    NOUN = "N"  # اسم
    VERB = "V"  # فعل
    ADJECTIVE = "A"  # صفة
    ADVERB = "D"  # ظرف
    PRONOUN = "P"  # ضمير
    INTERJECTION = "I"  # انفعال
    PARTICLE = "R"  # أداة

class ExampleType(str, Enum):
    """Types of examples."""
    QUOTE = "quote"  # نص مقتبس
    EXAMPLE = "example"  # مثال
    IDIOM = "idiom"  # مثل
    PROVERB = "proverb"  # حكمة
    SAYING = "saying"  # مقولة
    QURANIC = "quranic"  # قرآني
    QURANIC_READING = "Quranicreading"  # قراءة قرآنية
    HADITH = "hadith"  # حديث
    OTHER = "other"  # آخر

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
    lexical_entry_id: str
    lexicon_id: str
    lexicon_name: str
    lemma: str
    lemma_type: LemmaType
    lemma_audio: Optional[str]
    pattern: str
    senses: List[Sense] = field(default_factory=list)
    pos: PartOfSpeech
    root: List[str] = field(default_factory=list)
    word_forms: List[WordForm] = field(default_factory=list)
    non_diacritics_lemma: str
    lemma_language: str
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
    id: str
    name: str
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

# Export all models
__all__ = [
    'LemmaType',
    'PartOfSpeech',
    'ExampleType',
    'WordForm',
    'Translation',
    'Example',
    'Sense',
    'SearchResult',
    'LexiconEntry',
]
