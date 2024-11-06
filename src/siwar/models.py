"""
Models for the Siwar API wrapper.
Defines dataclasses and enums for type-safe API interactions.
"""

from dataclasses import dataclass
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
    CONCRETE_NOUN = "NC"  # اسم ذات
    ABSTRACT_NOUN = "NA"  # اسم معنى
    PLACE_NOUN = "NL"  # اسم مكان
    TIME_NOUN = "NT"  # اسم زمان
    INSTRUMENT_NOUN = "NM"  # اسم آلة
    COLLECTIVE_NOUN = "NG"  # اسم جنس
    FORM_NOUN = "NF"  # اسم هيئة
    INSTANCE_NOUN = "NO"  # اسم مرة
    VAGUE_NOUN = "NI"  # اسم مبهم
    INTRANSITIVE_VERB = "VI"  # فعل لازم
    TRANSITIVE_VERB = "VT"  # فعل متعدٍّ
    RELATIVE_ADJECTIVE = "AR"  # منسوب
    ACTIVE_PARTICIPLE = "AS"  # صفة فاعل
    PASSIVE_PARTICIPLE = "AO"  # صفة مفعول
    COMPARATIVE = "AP"  # أفعل التفضيل
    ASSIMILATED = "AA"  # صفة مشبهة
    INTENSIFIER = "AX"  # صيغة مبالغة
    PERSONAL_PRONOUN = "PP"  # ضمير شخصي
    DEMONSTRATIVE = "PD"  # ضمير إشارة
    RELATIVE_PRONOUN = "PR"  # ضمير موصول
    PLACE_ADVERB = "DL"  # ظرف مكان
    TIME_ADVERB = "DT"  # ظرف زمان
    VERBAL_INTERJECTION = "IV"  # انفعال فعلي
    SOUND_INTERJECTION = "IS"  # انفعال صوت
    EXCLAMATION = "II"  # انفعال تعجب
    DISPRAISE = "IF"  # انفعال ذم
    PRAISE = "IP"  # انفعال مدح

class ExampleType(str, Enum):
    """Types of examples in dictionary entries."""
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
class Translation:
    """Translation of a word to another language."""
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
class WordForm:
    """Morphological form of a word."""
    form: str
    phonetic: Optional[str] = None
    dialect: Optional[str] = None
    audio: Optional[str] = None
    aspect: Optional[str] = None  # P, S, C for verb types
    definition: Optional[str] = None  # i, d, d1, d2 for definiteness
    gender: Optional[str] = None  # m, f, f1, f2
    number: Optional[str] = None  # 1, 2, 3, 3s, 3t for number
    person: Optional[str] = None  # 1, 2, 3
    voice: Optional[str] = None  # a, p for active/passive
    is_nasab: bool = False
    is_small: bool = False

@dataclass
class Sense:
    """Sense (meaning) of a word."""
    definition: str
    translations: List[Translation]
    contexts: List[str]
    domains: List[str]
    examples: List[Example]
    relations: List[Dict[str, str]]
    image: Optional[str] = None

@dataclass
class SearchResult:
    """Result from a search query."""
    lexical_entry_id: str
    lexicon_id: str
    lexicon_name: str
    lemma: str
    lemma_type: LemmaType
    lemma_audio: Optional[str]
    pattern: str
    senses: List[Sense]
    pos: PartOfSpeech
    root: List[str]
    word_forms: List[WordForm]
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
    """Entry in a lexicon."""
    id: str
    name: str
    title: Optional[str] = None
    version: Optional[str] = None
    version_date: Optional[str] = None
    is_published: bool = False
    publisher_name: Optional[str] = None
    description: Optional[str] = None
    domain_ids: List[str] = None
    status: str = "DRAFT"
    is_public: bool = False
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
