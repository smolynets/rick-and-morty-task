import os
import json
from typing import Any, Dict, List
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

    async def fetch_all_pages(self, endpoint: str) -> List[Dict[str, Any]]:
        """
        Fetch all pages of data for the given endpoint.
        """
        all_data = []
        next_page = f"{self.base_url}/{endpoint}"
        while next_page:
            response_data = await self.fetch(endpoint)
            all_data.extend(response_data['results'])
            next_page = response_data['info']['next']
            if next_page:
                endpoint = next_page.split(self.base_url + "/")[-1]
        return all_data

    async def save_to_json(self, type_name: str) -> None:
        """
        Save to JSON
        """
        data = await self.fetch_all_pages(type_name)
        os.makedirs("api_data", exist_ok=True)
        with open(f"api_data/{type_name}.json", 'w') as f:
            json.dump({"id": str(uuid.uuid4()), "count": len(data), "RawData": data}, f, indent=4)

    async def close(self):
        await self.client.aclose()
