from typing import Optional

from fastapi import FastAPI

app = FastAPI()


app.get("/")
async def mainpage():
    return {
        helloworld
    }
app.get("/server-list")
def serverlist():
    return {
        "code": 200,
        "data": {
            "official": [{"name": "test official server","online": 0}],
            "unofficial": [{"name": "test unofficial server","online": 0}]

        }
        
    }
