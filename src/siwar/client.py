# src/siwar/client.py
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
    ) -> Dict[str, Any]:
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
            return cast(Dict[str, Any], response.json())
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 401:
                raise SiwarAuthError("Invalid API key")
            raise SiwarAPIError(f"HTTP {e.response.status_code}: {e.response.text}")
        except requests.exceptions.RequestException as e:
            raise SiwarAPIError(f"Request failed: {str(e)}")
