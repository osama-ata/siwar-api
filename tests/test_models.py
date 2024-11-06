"""Test cases for the Siwar API models."""

from datetime import datetime
from siwar.models import (
    LemmaType,
    PartOfSpeech,
    ExampleType,
    WordForm,
    Translation,
    Example,
    Sense,
    SearchResult,
    LexiconEntry
)

def test_word_form():
    """Test WordForm model."""
    form = WordForm(
        form="محرك",
        phonetic="muharrik",
        dialect="MSA",
        audio=None
    )
    assert form.form == "محرك"
    assert form.phonetic == "muharrik"
    assert form.dialect == "MSA"
    assert form.audio is None

def test_search_result():
    """Test SearchResult model."""
    result = SearchResult(
        lexical_entry_id="123",
        lexicon_id="456",
        lexicon_name="Test Lexicon",
        lemma="محرك",
        lemma_type=LemmaType.SINGLE_WORD,
        pattern="فاعل",
        pos=PartOfSpeech.NOUN,
        non_diacritics_lemma="محرك",
        lemma_language="ar"
    )
    assert result.lexical_entry_id == "123"
    assert result.lemma == "محرك"
    assert result.lemma_type == LemmaType.SINGLE_WORD
    assert result.pos == PartOfSpeech.NOUN

def test_lexicon_entry():
    """Test LexiconEntry model."""
    entry = LexiconEntry(
        id="123",
        name="Test Lexicon",
        title="Test Title",
        version="1.0",
        is_published=True,
        created_at=datetime(2024, 1, 1)
    )
    assert entry.id == "123"
    assert entry.name == "Test Lexicon"
    assert entry.is_published is True
