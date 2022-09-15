from dbConnection import Dbconnection

try:
    async def insertModel(file, modelId):
        connect=Dbconnection()
        cursor=connect.singleStoreConnection()
        print(cursor)
        print(file)
        print(modelId)
        # cursor.execute(""" INSERT INTO model_files(id,model) VALUES (%s,%s)""",(str(modelId),file))

        getModels=cursor.execute(""" SELECT * FROM  model_files""")
        print(getModels)
        # cursor.commit() 

except Exception as e:
            print("Error:",str(e)) 