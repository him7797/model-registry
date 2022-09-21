from ast import Delete
from typing import Union
from fastapi import FastAPI, File, Form, UploadFile
from pydantic import BaseModel
import sys
import uuid
# adding Folder_2 to the system path
sys.path.insert(0, 'C:/Users/kssh/model-registry/database')
from modelRegistry import insertModel, insertModelInformation,getModelId,getAllModels,deleteModelId1,deleteModelId2,getAllModelsssss
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
    return {"Hello": "Welcome to model regisrty"}
#1. Test-image 
#@app.post("/upload-model")
@app.post("/upload-model")
async def uploadModelFile(file: bytes = File()):
    id = uuid.uuid4()
    await insertModel(file,id)
    print(file)
    print(id)
    return {"message":"success","modelID":id}
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
@app.get("/model/{id}")
async def modelId(id):   
    result=await getModelId(id)   
    return {"message":"success","model":result}
#5. Model/test/:id 
@app.get("/model")
async def model():   
    result = await getAllModels()   
    return {"message":"success","allModels":result}
#7. Model/:id Delete
@app.delete("/model/{id}")
async def modelIdDelete(id):   
    result1=await deleteModelId1(id)   
    result2=await deleteModelId2(id)   
    result=result1+result2
    return {"message":"success","model":result}
#8. Zip-file 
@app.get("/modelsss")
async def model():   
    result = await getAllModelsssss()   
    return {"message":"success","allModels":result}


# async with aiofiles.open('D:/EDGEAI/model-registry', 'wb') as out_file:
#         content = await in_file.read()  # async read
#         await out_file.write(content)  # async write

#     return {"Result": "OK"}










