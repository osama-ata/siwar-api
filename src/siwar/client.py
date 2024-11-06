"""Siwar API client implementation."""

from typing import List, Optional, Dict, Any, cast
import requests

from .exceptions import SiwarAPIError, SiwarAuthError
from .models.core import SearchResult, LexiconEntry
from .constants import API_BASE_URL, DEFAULT_TIMEOUT


class SiwarClient:
    """A Python client for the Siwar API."""
    
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
            
        data = self._make_request(
            'GET', 
            '/api/v1/external/public/search', 
            params=params
        )
        return [SearchResult(**result) for result in data]

    def search_private(
        self, 
        query: str, 
        lexicon_ids: List[str]
    ) -> List[SearchResult]:
        """
        Search in private entries.
        
        Args:
            query: The query string to search for
            lexicon_ids: List of lexicon IDs to search in (required)
            
        Returns:
            List of search results
        """
        params = {
            'query': query,
            'lexiconIds': ','.join(lexicon_ids)
        }
        data = self._make_request(
            'GET', 
            '/api/v1/external/private/search', 
            params=params
        )
        return [SearchResult(**result) for result in data]

    def get_public_lexicons(self) -> List[LexiconEntry]:
        """
        Get all public lexicons.
        
        Returns:
            List of lexicon entries
        """
        data = self._make_request('GET', '/api/v1/external/public/lexicons')
        return [LexiconEntry(**lexicon) for lexicon in data]

    def get_entry_senses(
        self, 
        query: str, 
        lexicon_ids: Optional[List[str]] = None,
        private: bool = False
    ) -> Dict:
        """
        Get entry senses.
        
        Args:
            query: The query string
            lexicon_ids: List of lexicon IDs (required for private search)
            private: Whether to search in private lexicons
            
        Returns:
            Entry senses information
        """
        access_type = 'private' if private else 'public'
        params = {'query': query}
        if lexicon_ids or private:
            params['lexiconIds'] = ','.join(lexicon_ids)
            
        return self._make_request(
            'GET', 
            f'/api/v1/external/{access_type}/senses',
            params
        )
