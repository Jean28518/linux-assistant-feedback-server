from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
import json

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
    feedback_string = json.dumps(feedback, indent=4)
    # f.write(feedback.json(indent=4))
    f.write(feedback_string)
    f.close()

    
    return {"message": "success"}