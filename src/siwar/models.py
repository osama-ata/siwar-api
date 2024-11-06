"""Models for the Siwar API wrapper."""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import List, Optional, Dict

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
    domain_ids: List[str] = field(default_factory=list)
    status: str = "DRAFT"
    is_public: bool = False
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
