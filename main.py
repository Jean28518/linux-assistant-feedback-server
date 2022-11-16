from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

class Feedback(BaseModel):
    message: str
    entries: list
    searchTerm: str
    environment : dict


app = FastAPI()

@app.post("/submit/")
async def submit(feedback: Feedback):
    now = datetime.now()
    file_name = now.strftime("%Y-%m-%d_%H:%M:%S") + ".json"
    f = open("./feedback/" + file_name, "a")
    f.write(feedback.json(indent=4))
    f.close()

    
    return {"message": "success"}