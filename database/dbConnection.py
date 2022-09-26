from configHandler import ConfigHandler
from mysql.connector import errorcode, connect


class Dbconnection():
    def singleStoreConnection(self):
        try:
            getInfo = ConfigHandler()
            getConnectionData = getInfo.getMemesqlConfig()
            print(getConnectionData)
            host = getConnectionData['Memsql_Config']['host']
            port = getConnectionData['Memsql_Config']['port']
            username = getConnectionData['Memsql_Config']['username']
            password = getConnectionData['Memsql_Config']['password']
            database = getConnectionData['Memsql_Config']['database']
            print(host + " " + port + " " + username +
                  " " + password + " " + database)
            dbConnection = connect(
                user=username, password=password, database=database, host=host, port=port)
            cursor = dbConnection.cursor()
            return cursor
        except Exception as e:
            print("Error:", str(e))
