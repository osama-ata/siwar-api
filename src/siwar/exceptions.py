"""
Exceptions for the Siwar API wrapper.
"""

class SiwarAPIError(Exception):
    """Base exception for Siwar API errors."""
    
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


class SiwarAuthError(SiwarAPIError):
    """Raised when authentication with the API fails."""
    pass


class SiwarValueError(SiwarAPIError):
    """Raised when invalid values are provided to API methods."""
    pass


class SiwarResponseError(SiwarAPIError):
    """Raised when API response cannot be parsed."""
    pass


class SiwarTimeoutError(SiwarAPIError):
    """Raised when API request times out."""
    pass


class SiwarRateLimitError(SiwarAPIError):
    """Raised when API rate limit is exceeded."""
    pass
