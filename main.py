from typing import Union
from fastapi import FastAPI, File, Form, UploadFile
from pydantic import BaseModel
import sys
import uuid
 
# adding Folder_2 to the system path
sys.path.insert(0, '/home/himanshu/Documents/modelRegistry/database')
from modelRegistry import insertModel, insertModelInformation

app = FastAPI()


class SaveModel(BaseModel):
    name: str
    categoryId:str
    modelId:str
    description:str
    version:str
    modelBasicInfoData: dict
    parameterInfoData: dict
    metricsInfoData: dict
    tags: dict
    featuresInfoData: dict
    localInference: bool
    createdBy: str
    stage:str
    liveStatus:str
             
        

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_id": item_id}


@app.post("/upload-model")
async def uploadModelFile(file: bytes = File()):
    id = uuid.uuid4()
    await insertModel(file,id)
    print(file)
    print(id)
    return {"message":"success"}

@app.post("/save-model")
async def saveModelInfo(saveModel: SaveModel):
    id = uuid.uuid4()
    await insertModelInformation(id,saveModel.name,
        saveModel.categoryId,
        saveModel.modelId,
        saveModel.description,
        saveModel.version,
        saveModel.modelBasicInfoData,
        saveModel.parameterInfoData,
        saveModel.metricsInfoData,
        saveModel.tags,
        saveModel.featuresInfoData,
        saveModel.localInference,
        saveModel.createdBy,
        saveModel.stage,
        saveModel.liveStatus)

    return {"message":"success"}
   


