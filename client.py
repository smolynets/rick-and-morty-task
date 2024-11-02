import os
import json
from typing import Any, Dict
import uuid

import httpx


class RickAndMortyAPIClient:

    def __init__(self, base_url: str):
        self.client = httpx.AsyncClient()
        self.base_url = base_url

    async def fetch(self, endpoint: str) -> Dict[str, Any]:
        """
        Fetch data or raise exception
        """
        response = await self.client.get(f"{self.base_url}/{endpoint}")
        response.raise_for_status()
        return response.json()

    async def save_to_json(self, type_name: str) -> None:
        """
        Save to JSON
        """
        data = await self.fetch(type_name)
        os.makedirs("api_data", exist_ok=True)
        with open(f"api_data/{type_name}.json", 'w') as f:
            json.dump({"id": str(uuid.uuid4()), "RawData": data}, f, indent=4)

    async def close(self):
        await self.client.aclose()
