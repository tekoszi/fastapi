from fastapi import FastAPI
from fastapi.responses import JSONResponse

from bson.objectid import ObjectId
import json
from pymongo import MongoClient
from bson import json_util

app = FastAPI()

MONGODB_HOST = 'mongodb'
MONGODB_PORT = 27017
DB_NAME = 'games'
COLLECTION_NAME = 'games'



@app.get("/")
def home():
    return {"hello": "world"}


@app.get("/get_games")
async def get_games():
    try:
        connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
        collection = connection[DB_NAME][COLLECTION_NAME]
        games = collection.find()
        game_list = []
        for game in games:
            game_list.append(game)
        json_games = json.dumps(game_list, default=json_util.default)
        return json_games
    except:
        pass
    finally:
        connection.close()

@app.get("/game/{obj_id}")
async def get_game(obj_id:str):
    try:
        connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
        collection = connection[DB_NAME][COLLECTION_NAME]
        game = collection.find({"_id": "61436c1254121b913ec29b7d"})

        games = collection.find({"_id": ObjectId("61436c1254121b913ec29b7d")})

        return games
    except:
        pass
    finally:
        connection.close()
