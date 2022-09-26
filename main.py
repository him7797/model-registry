
from ast import Delete
from typing import Union
from fastapi import FastAPI, File, Form, UploadFile, status
from pydantic import BaseModel
import sys
import uuid
from fastapi.exceptions import HTTPException
import aiofiles
import os
import zipfile
CHUNK_SIZE = 1024 * 1024  # adjust the chunk size as desired
# adding Folder_2 to the system path
sys.path.insert(0, '/home/himanshu/Documents/model-registry/database')
from modelRegistry import insertModel, insertModelInformation, getModelId, getAllModels, deleteModelId1, deleteModelId2, getAllModelsssss, getModelByVersion
app = FastAPI()


class SaveModel(BaseModel):
    name: str
    categoryId: str
    modelId: str
    description: str
    version: str
    modelBasicInfoData: dict
    parameterInfoData: dict
    metricsInfoData: dict
    tags: dict
    featuresInfoData: dict
    localInference: bool
    createdBy: str
    stage: str
    liveStatus: str


@app.get("/")
def read_root():
    return {"Hello": "Welcome to model regisrty"}
# 1. Test-image
# @app.post("/upload-model")


@app.post("/upload-model")
async def uploadModelFile(file: bytes = File()):
    id = uuid.uuid4()
    await insertModel(file, id)
    print(id)
    return {"message": "success", "modelID": id}


@app.post("/save-model")
async def saveModelInfo(saveModel: SaveModel):
    id = uuid.uuid4()
    await insertModelInformation(id, saveModel.name,
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
    return {"message": "success"}


@app.get("/model/{id}")
async def modelId(id):
    result = await getModelId(id)
    return {"message": "success", "model": result}
# 5. Model/test/:id


@app.get("/model")
async def model():
    result = await getAllModels()
    return {"message": "success", "allModels": result}
# 7. Model/:id Delete


@app.delete("/model/{id}")
async def modelIdDelete(id):
    result1 = await deleteModelId1(id)
    result2 = await deleteModelId2(id)
    result = result1+result2
    return {"message": "success", "model": result}
# 8. Zip-file


@app.get("/modelsss")
async def model():
    result = await getAllModelsssss()
    return {"message": "success", "allModels": result}



@app.get("/model/{id}")
async def modelId(id):
    result = await getModelId(id)
    return {"message": "success", "model": result}



# @app.post("/zip-file")
# async def zipFIleUpload(zipFile: bytes = File()):
#     nlkn="l"


@app.get("/model/version")
async def getModelbyVersion(modelId:str,modelVersion:str):
    result=await getModelByVersion(modelId,modelVersion)
    return {"message":"success",model:result}

    

# async with aiofiles.open('D:/EDGEAI/model-registry', 'wb') as out_file:
#         content = await in_file.read()  # async read
#         await out_file.write(content)  # async write

#     return {"Result": "OK"}







@app.post("/zip-file")
async def upload(file: UploadFile = File(...)):
    try:
        print(len(file))
        os.mkdir('./uploads')
        os.mkdir('./uploads/zip/')
        filepath = os.path.join('./uploads', os.path.basename(file.filename))
        async with aiofiles.open(filepath, 'wb') as f:
            while chunk := await file.read(CHUNK_SIZE):
                await f.write(chunk)
        with zipfile.ZipFile('./uploads/'+file.filename, 'r') as zip_ref:
            zip_ref.extractall('./uploads/zip/')
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail='There was an error uploading the file')
    finally:
        await file.close()

    return {"message": f"Successfuly uploaded {file.filename}"}