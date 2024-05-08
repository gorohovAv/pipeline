from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter, Response
from src.database import get_db

class Stage(BaseModel):
    stage_name: str
    stage_content: list[str]

class GitlabCD():
    def __init__(self, stage: Stage):
        self.stage_name = stage.stage_name
        self.stage_content = stage.stage_content

    def __str__(self):
        return f'''{self.stage_name}:
                  {str([(x+"\n") for x in self.stage_content])}'''

app = FastAPI()

@app.post("/makeCD")
async def make_gitlab_cd(stage: Stage, db: Session = Depends(get_db)):
    cicd = str(GitlabCD(stage))
    await db.add(cicd)
    return str(cicd)





