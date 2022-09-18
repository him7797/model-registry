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

