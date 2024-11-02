from fastapi import FastAPI

from client import RickAndMortyAPIClient


app = FastAPI()
client = RickAndMortyAPIClient("https://rickandmortyapi.com/api")


@app.get(
    "/fetch-data/",
    summary="Fetch all data",
    description="Fetch all data for characters, locations and episodes and save it in json files"
)
async def fetch_data():
    await client.save_to_json("character")
    await client.save_to_json("location")
    await client.save_to_json("episode")
    return {"message": "Data fetched and saved successfully."}


@app.get(
    "/episode-names/{start_year}/{end_year}",
    summary="Get filtered episode names",
    description="Get name of episodes beetwen particular years"
)
async def get_episodes_between(start_year: int, end_year: int):
    episodes = await client.fetch("episode")
    names = [
        episode["name"] 
        for episode in episodes["results"]
        if start_year <= int(episode["created"].split("-")[0]) <= end_year
    ]
    return {"episode_names": names}


@app.on_event("shutdown")
async def shutdown_event():
    await client.close()
