import json


class ConfigHandler():
    def initJson(self, filename):
        try:
            with open(filename) as json_data_file:
                data = json.load(json_data_file)
            return data
        except Exception as e:
            print("Error")
            print(e)

    def getMemesqlConfig(self):
        return self.initJson('/home/himanshu/Documents/modelRegistry/database/memsqlConfig.json')
