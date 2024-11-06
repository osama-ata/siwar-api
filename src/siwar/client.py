"""
Siwar API client implementation.
Provides the main interface for interacting with the Siwar API.
"""

import requests
from typing import List, Optional, Dict, Any, Union
from .exceptions import SiwarAPIError, SiwarAuthError
from .models import SearchResult, LexiconEntry
from .constants import API_BASE_URL

class SiwarClient:
    """
    A Python client for the Siwar API.
    
    Args:
        api_key (str): Your Siwar API key
        base_url (str, optional): Base URL for the API. Defaults to API_BASE_URL
        timeout (int, optional): Request timeout in seconds. Defaults to 30
    """
    
    def __init__(self, api_key: str, base_url: str = API_BASE_URL, timeout: int = 30):
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
        params: Optional[Dict] = None,
        data: Optional[Dict] = None
    ) -> Any:
        """
        Make HTTP request to the API.
        
        Args:
            method: HTTP method (GET, POST, etc.)
            endpoint: API endpoint
            params: Query parameters
            data: Request body data
            
        Returns:
            API response data
            
        Raises:
            SiwarAuthError: If authentication fails
            SiwarAPIError: If API request fails
        """
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
            
        data = self._make_request('GET', '/api/v1/external/public/search', params)
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
        data = self._make_request('GET', '/api/v1/external/private/search', params)
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

    def get_entry_examples(
        self, 
        query: str, 
        lexicon_ids: Optional[List[str]] = None,
        private: bool = False
    ) -> Dict:
        """Get entry examples."""
        access_type = 'private' if private else 'public'
        params = {'query': query}
        if lexicon_ids or private:
            params['lexiconIds'] = ','.join(lexicon_ids)
            
        return self._make_request(
            'GET', 
            f'/api/v1/external/{access_type}/examples',
            params
        )

    def get_entry_synonyms(
        self, 
        query: str, 
        lexicon_ids: Optional[List[str]] = None,
        private: bool = False
    ) -> Dict:
        """Get entry synonyms."""
        access_type = 'private' if private else 'public'
        params = {'query': query}
        if lexicon_ids or private:
            params['lexiconIds'] = ','.join(lexicon_ids)
            
        return self._make_request(
            'GET', 
            f'/api/v1/external/{access_type}/synonyms',
            params
        )

    def get_entry_opposites(
        self, 
        query: str, 
        lexicon_ids: Optional[List[str]] = None,
        private: bool = False
    ) -> Dict:
        """Get entry opposites."""
        access_type = 'private' if private else 'public'
        params = {'query': query}
        if lexicon_ids or private:
            params['lexiconIds'] = ','.join(lexicon_ids)
            
        return self._make_request(
            'GET', 
            f'/api/v1/external/{access_type}/opposites',
            params
        )

    def get_entry_pos(
        self,
        query: str,
        lexicon_ids: Optional[List[str]] = None,
        private: bool = False
    ) -> Dict:
        """Get entry part of speech information."""
        access_type = 'private' if private else 'public'
        params = {'query': query}
        if lexicon_ids or private:
            params['lexiconIds'] = ','.join(lexicon_ids)
            
        return self._make_request(
            'GET',
            f'/api/v1/external/{access_type}/pos',
            params
        )

    def get_entry_root(
        self,
        query: str,
        lexicon_ids: Optional[List[str]] = None,
        private: bool = False
    ) -> Dict:
        """Get entry root information."""
        access_type = 'private' if private else 'public'
        params = {'query': query}
        if lexicon_ids or private:
            params['lexiconIds'] = ','.join(lexicon_ids)
            
        return self._make_request(
            'GET',
            f'/api/v1/external/{access_type}/root',
            params
        )

    def get_entry_pattern(
        self,
        query: str,
        lexicon_ids: Optional[List[str]] = None,
        private: bool = False
    ) -> Dict:
        """Get entry pattern information."""
        access_type = 'private' if private else 'public'
        params = {'query': query}
        if lexicon_ids or private:
            params['lexiconIds'] = ','.join(lexicon_ids)
            
        return self._make_request(
            'GET',
            f'/api/v1/external/{access_type}/pattern',
            params
        )

    def get_entry_conjugations(
        self,
        query: str,
        lexicon_ids: Optional[List[str]] = None,
        private: bool = False
    ) -> Dict:
        """
        Get entry conjugations/word forms.
        
        Args:
            query: Word to get conjugations for
            lexicon_ids: Optional list of lexicon IDs
            private: Whether to search private lexicons
            
        Returns:
            Dictionary containing conjugation information
        """
        access_type = 'private' if private else 'public'
        params = {'query': query}
        if lexicon_ids or private:
            params['lexiconIds'] = ','.join(lexicon_ids)
            
        return self._make_request(
            'GET',
            f'/api/v1/external/{access_type}/conjugations',
            params
        )
