import requests
from .src.index import exports as MODULES

class SellAuthError(Exception):
    """Custom exception for SellAuth API errors."""
    pass

class SellAuthClient:
    def __init__(self, api_key: str, base_url: str = "https://api.sellauth.com"):
        if not api_key:
            raise ValueError("API key is required")

        self.api_key = api_key
        self.base_url = base_url.rstrip("/")

        for name, module_cls in MODULES.items():
            setattr(self, name.lower(), module_cls(self))

    def request(self, method: str, endpoint: str, data=None, params=None):
        """
        Generic request method used by all modules.
        Supports GET, POST, PUT, DELETE requests.
        """
        url = f"{self.base_url}{endpoint}"

        try:
            response = requests.request(
                method=method.upper(),
                url=url,
                json=data or {},
                params=params or {},
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json",
                    "Accept": "application/json"
                },
                timeout=30
            )
        except requests.RequestException as e:
            raise SellAuthError(f"Request error: {e}") from e

        if not response.ok:
            try:
                error_data = response.json()
                message = error_data.get("message", response.text)
            except ValueError:
                message = response.text
            raise SellAuthError(f"HTTP {response.status_code}: {message}")

        try:
            return response.json()
        except ValueError:
            return response.text
