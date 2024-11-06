"""Test cases for the Siwar API client."""

import pytest
import responses
from siwar import SiwarClient, SiwarAPIError, SiwarAuthError

API_KEY = "test_api_key"
BASE_URL = "https://api.siwar.ksaa.gov.sa"

@pytest.fixture
def client():
    """Create a test client."""
    return SiwarClient(API_KEY, BASE_URL)

@responses.activate
def test_search_public(client):
    """Test public search endpoint."""
    # Mock response data
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
    
    # Register mock response
    responses.add(
        responses.GET,
        f"{BASE_URL}/api/v1/external/public/search",
        json=mock_response,
        status=200
    )
    
    # Make request
    results = client.search_public("محرك")
    
    # Verify response
    assert len(results) == 1
    assert results[0].lexical_entry_id == "123"
    assert results[0].lemma == "محرك"

@responses.activate
def test_auth_error(client):
    """Test authentication error handling."""
    responses.add(
        responses.GET,
        f"{BASE_URL}/api/v1/external/public/search",
        status=401
    )
    
    with pytest.raises(SiwarAuthError):
        client.search_public("test")

@responses.activate
def test_api_error(client):
    """Test API error handling."""
    responses.add(
        responses.GET,
        f"{BASE_URL}/api/v1/external/public/search",
        status=500
    )
    
    with pytest.raises(SiwarAPIError):
        client.search_public("test")

@responses.activate
def test_get_public_lexicons(client):
    """Test get public lexicons endpoint."""
    mock_response = [
        {
            "id": "123",
            "name": "Test Lexicon",
            "title": "Test Title",
            "version": "1.0",
            "is_published": True
        }
    ]
    
    responses.add(
        responses.GET,
        f"{BASE_URL}/api/v1/external/public/lexicons",
        json=mock_response,
        status=200
    )
    
    lexicons = client.get_public_lexicons()
    assert len(lexicons) == 1
    assert lexicons[0].id == "123"
    assert lexicons[0].name == "Test Lexicon"
