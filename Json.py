import json

class Json:
    @staticmethod
    def read():
        with open(Files.promocobes, "r") as file:
            return json.load(file) 
    
    @staticmethod
    def write(data):
        with open(Files.promocobes, "w") as file:
            json.dump(data, file)
 