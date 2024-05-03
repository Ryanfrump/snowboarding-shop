from fastapi import FastAPI
import json

from models import Snowboard



app = FastAPI()

with open("snowboards.json", "r") as f:
    snowboard_list = json.load(f)

snowboards: list[Snowboard] = []

for snowboard in snowboard_list:
    snowboards.append(Snowboard(**snowboard))

@app.get("/snowboard")
async def list_snowboard() -> list[Snowboard]:
    return snowboards

@app.post("/snowboard")
async def add_snowboard(snowboard: Snowboard):
    snowboards.append(snowboard)

@app.put("/snowboard/{snowboard_id}")
async def update_snowboard(snowboard_id: int, new_snowboard: Snowboard):
    for i, snowboard in enumerate(snowboards):
        if snowboard.id == snowboard_id:
            snowboards[i] = new_snowboard
            return
    snowboards.append(new_snowboard)
    return
        
@app.delete("/snowboard/{snowboard_id}")
async def delete_snowboard(snowboard_id: int):
    for i, snowboard in enumerate(snowboards):
        if snowboard.id == snowboard_id:
            snowboards.pop(i)
            return
    
