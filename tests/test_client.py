"""Test cases for the Siwar API public endpoints."""

import os
import pytest
import responses
from siwar import SiwarClient, SiwarAPIError, SiwarAuthError
from siwar.constants import PUBLIC_ENDPOINTS, API_BASE_URL

# Get API key from environment variable
API_KEY = os.getenv("SIWAR_API_KEY", "test_api_key")

@pytest.fixture
def client():
    """Create a test client."""
    return SiwarClient(API_KEY, API_BASE_URL)

@responses.activate
def test_search_public(client):
    """Test public search endpoint."""
    mock_response = [
        {
            "lexical_entry_id": "123",
            "lexicon_id": "456",
            "lexicon_name": "Test Lexicon",
            "lemma": "محرك",
            "lemma_type": "singleWord",
            "pattern": "فاعل",
            "pos": "N",
            "non_diacritics_lemma": "محرك",
            "lemma_language": "ar",
            "lemma_audio": None,
            "senses": []
        }
    ]
    
    responses.add(
        responses.GET,
        f"{API_BASE_URL}{PUBLIC_ENDPOINTS['search']}",
        json=mock_response,
        status=200
    )
    
    results = client.search_public("محرك")
    assert len(results) == 1
    assert results[0].lexical_entry_id == "123"
    assert results[0].lemma == "محرك"

@responses.activate
def test_get_public_lexicons(client):
    """Test public lexicons endpoint."""
    mock_response = [
        {
            "id": "123",
            "name": "Test Lexicon",
            "title": "Test Title",
            "is_published": True
        }
    ]
    
    responses.add(
        responses.GET,
        f"{API_BASE_URL}{PUBLIC_ENDPOINTS['lexicons']}",
        json=mock_response,
        status=200
    )
    
    lexicons = client.get_public_lexicons()
    assert len(lexicons) == 1
    assert lexicons[0].id == "123"
    assert lexicons[0].name == "Test Lexicon"

@responses.activate
def test_get_public_senses(client):
    """Test public senses endpoint."""
    mock_response = [
        {
            "definition": "Test definition",
            "translations": [],
            "contexts": [],
            "domains": [],
            "examples": [],
            "relations": []
        }
    ]
    
    responses.add(
        responses.GET,
        f"{API_BASE_URL}{PUBLIC_ENDPOINTS['senses']}",
        json=mock_response,
        status=200
    )
    
    senses = client.get_public_senses("محرك")
    assert len(senses) == 1
    assert senses[0].definition == "Test definition"

def test_private_endpoints_not_implemented(client):
    """Test that private endpoints raise NotImplementedError."""
    with pytest.raises(NotImplementedError):
        client._private_endpoint_warning()
