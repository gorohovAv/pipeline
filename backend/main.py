from fastapi import FastAPI
from pydantic import BaseModel

class Stage(BaseModel):
    stage_name: str
    stage_content: list[str]
class Pipeline(BaseModel):
    pass

class GitlabCD():
    def __init__(self, stage: Stage):
        self.stage_name = stage.stage_name
        self.stage_content = stage.stage_content

    def __str__(self):
        return f'''{self.stage_name}:
                  {str([(x+"\n") for x in self.stage_content])}'''

app = FastAPI()

@app.post("/makeCD")
async def make_gitlab_cd(stage: Stage):
    cicd = GitlabCD(stage)
    return str(cicd)
