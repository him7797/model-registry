from dbConnection import Dbconnection
from configHandler import ConfigHandler
from mysql.connector import connect
import json
getInfo=ConfigHandler()
getConnectionData=getInfo.getMemesqlConfig()
print(getConnectionData)
host=getConnectionData['Memsql_Config']['host']
port=getConnectionData['Memsql_Config']['port']
username=getConnectionData['Memsql_Config']['username']
password=getConnectionData['Memsql_Config']['password']
database=getConnectionData['Memsql_Config']['database']
print(host + " "+ port+ " "+ username + " "+ password + " "+ database)
dbConnection=connect(user=username, password=password, database=database, host=host, port=port)
async def insertModel(file, modelId):
        # cursor.execute(""" INSERT INTO model_files(id,model) VALUES (%s,%s)""",(str(modelId),file))
    try:
        cursor = dbConnection.cursor()
        insertModelFile=""" INSERT INTO model_files
                          (id,model) VALUES (%s,%s)"""
        insert_blob_tuple = ( str(modelId),file )
        result = cursor.execute(insertModelFile, insert_blob_tuple)
        dbConnection.commit()
        # cursor.commit() 
    except Exception as e:
            print("Error:",str(e)) 
async def insertModelInformation(id,name,
        categoryId,
        modelId,
        description,
        version,
        modelBasicInfoData,
        parameterInfoData,
        metricsInfoData,
        tags,
        featuresInfoData,
        localInference,
        createdBy,
        stage,
        liveStatus):
        # cursor.execute(""" INSERT INTO model_files(id,model) VALUES (%s,%s)""",(str(modelId),file))
    try:
        cursor = dbConnection.cursor()
        insertModelFileInfo=""" INSERT INTO models
                          (id,
                          name,
                          categoryId,
                          modelFile,
                          description,
                          version,
                          createdBy,
                          stage,
                          localInference,
                          liveStatus,
                          modelBasicInfoData,
                          parameterInfoData,
                          metricsInfoData,
                          tags,
                          featuresInfoData) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        insert_mode_file_info = ( str(id),str(name),str(categoryId),str(modelId),str(description),str(version),str(createdBy),str(stage),localInference,str(liveStatus),json.dumps(modelBasicInfoData),json.dumps(parameterInfoData),json.dumps(metricsInfoData),json.dumps(tags),json.dumps(featuresInfoData))
        result = cursor.execute(insertModelFileInfo, insert_mode_file_info)
        dbConnection.commit()
        # cursor.commit() 
    except Exception as e:
            print("Error:",str(e)) 
async def getModelId(id):
    try:
        cursor = dbConnection.cursor()
        print(type(id))
        getModelIdFileInfo="select * from models where modelFile=%s"
        get_mode_file_info=(id,)
        cursor.execute(getModelIdFileInfo,get_mode_file_info)
        result=cursor.fetchall()
        print(result)
        # cursor.commit() 
        return result
    except Exception as e:
        print("Error:",str(e)) 
async def getAllModels():
    try:
        cursor = dbConnection.cursor()
        getModelIdFileInfo=""" select * from models """
        cursor.execute(getModelIdFileInfo)
        result=cursor.fetchall()
        # cursor.commit() 
        return result
    except Exception as e:
            print("Error:",str(e)) 
async def deleteModelId1(id):
    try:
        cursor = dbConnection.cursor()
        print(type(id))
        getModelIdFileInfo="DELETE FROM models WHERE modelFile=%s"
        get_mode_file_info=(id,)
        cursor.execute(getModelIdFileInfo,get_mode_file_info)
        cursor.close()
        result="Deletion sucessful in models. "
        # cursor.commit() 
        return result
    except Exception as e:
        print("Error:",str(e))
async def deleteModelId2(id):
    try:
        cursor = dbConnection.cursor()
        print(type(id))
        cursor = dbConnection.cursor()
        getModelIdFileInfo2="DELETE FROM model_files WHERE id=%s"
        get_mode_file_info2=(id,)
        cursor.execute(getModelIdFileInfo2,get_mode_file_info2)
        cursor.close()
        result="Deletion sucessful in model_files"
        # cursor.commit() 
        return result
    except Exception as e:
        print("Error:",str(e)) 
async def getAllModelsssss():
    try:
        cursor = dbConnection.cursor()
        getModelIdFileInfo=""" select id from model_files """
        cursor.execute(getModelIdFileInfo)
        result=cursor.fetchall()
        # cursor.commit() 
        return result
    except Exception as e:
            print("Error:",str(e))