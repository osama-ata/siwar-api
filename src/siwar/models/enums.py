"""Enum definitions for the Siwar API wrapper."""

from enum import Enum


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
