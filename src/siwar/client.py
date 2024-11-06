"""Siwar API client implementation."""

from typing import List, Optional, Dict, Any, cast
import requests

from .exceptions import SiwarAPIError, SiwarAuthError
from .models.core import SearchResult, LexiconEntry, Example, Sense
from .constants import (
    API_BASE_URL, 
    DEFAULT_TIMEOUT, 
    PUBLIC_ENDPOINTS
)


class SiwarClient:
    """
    A Python client for the Siwar API.
    
    Currently implements public endpoints only. Private endpoints will be added in future versions.
    """
    
    def __init__(
        self,
        api_key: str,
        base_url: str = API_BASE_URL,
        timeout: int = DEFAULT_TIMEOUT
    ) -> None:
        """Initialize the client."""
        self.api_key = api_key
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            'apikey': self.api_key,
            'Accept': 'application/json'
        })

    def _make_request(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict[str, str]] = None,
        data: Optional[Dict[str, Any]] = None
    ) -> Any:
        """Make HTTP request to the API."""
        url = f"{self.base_url}{endpoint}"

        try:
            response = self.session.request(
                method=method,
                url=url,
                params=params,
                json=data,
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 401:
                raise SiwarAuthError("Invalid API key")
            raise SiwarAPIError(f"HTTP {e.response.status_code}: {e.response.text}")
        except requests.exceptions.RequestException as e:
            raise SiwarAPIError(f"Request failed: {str(e)}")

    def search_public(
        self, 
        query: str, 
        lexicon_ids: Optional[List[str]] = None
    ) -> List[SearchResult]:
        """
        Search in public entries.
        
        Args:
            query: The query string to search for
            lexicon_ids: Optional list of lexicon IDs to search in
            
        Returns:
            List of search results
        """
        params = {'query': query}
        if lexicon_ids:
            params['lexiconIds'] = ','.join(lexicon_ids)
            
        data = self._make_request('GET', PUBLIC_ENDPOINTS['search'], params=params)
        return [SearchResult(**result) for result in data]

    def get_public_lexicons(self) -> List[LexiconEntry]:
        """
        Get all public lexicons.
        
        Returns:
            List of lexicon entries
        """
        data = self._make_request('GET', PUBLIC_ENDPOINTS['lexicons'])
        return [LexiconEntry(**lexicon) for lexicon in data]

    def get_public_senses(
        self, 
        query: str, 
        lexicon_ids: Optional[List[str]] = None
    ) -> List[Sense]:
        """
        Get sense information for a word from public lexicons.
        
        Args:
            query: The word to look up
            lexicon_ids: Optional list of lexicon IDs to search in
            
        Returns:
            List of word senses
        """
        params = {'query': query}
        if lexicon_ids:
            params['lexiconIds'] = ','.join(lexicon_ids)
            
        data = self._make_request('GET', PUBLIC_ENDPOINTS['senses'], params=params)
        return [Sense(**sense) for sense in data]

    def get_public_examples(
        self, 
        query: str, 
        lexicon_ids: Optional[List[str]] = None
    ) -> List[Example]:
        """
        Get example usages of a word from public lexicons.
        
        Args:
            query: The word to look up
            lexicon_ids: Optional list of lexicon IDs to search in
            
        Returns:
            List of examples
        """
        params = {'query': query}
        if lexicon_ids:
            params['lexiconIds'] = ','.join(lexicon_ids)
            
        data = self._make_request('GET', PUBLIC_ENDPOINTS['examples'], params=params)
        return [Example(**example) for example in data]

    # TODO: Implement other public endpoints:
    # - get_public_synonyms
    # - get_public_opposites
    # - get_public_pos
    # - get_public_root
    # - get_public_pattern
    # - get_public_conjugations

    def _private_endpoint_warning(self) -> None:
        """Raise warning about unimplemented private endpoints."""
        raise NotImplementedError(
            "Private endpoints are not implemented in this version. "
            "They will be added in a future release."
        )
