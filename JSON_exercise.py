# Exercise 1: Convert the following dictionary into JSON format

import json

data = {"key1" : "value1", "key2" : "value2"}

jsonData = json.dumps(data)
print(jsonData)

# Exercise 2: Access the value of key2 from the following JSON

import json

sampleJson = """{"key1": "value1", "key2": "value2"}"""

data = json.loads(sampleJson)
print(data['key2'])
print(type(sampleJson),type(data))

# Exercise 3: PrettyPrint following JSON data

import json

sampleJson = {"key1" : "value2", "key2" : "value2", "key3" : "value3"}
prettyPrintedJson  = json.dumps(sampleJson, indent=2, separators=(",", " = "))
print(prettyPrintedJson)

# Exercise 4: Sort JSON keys in and write them into a file

import json

sampleJson = {"id" : 1, "name" : "value2", "age" : 29}

with open("sampleJson.json", "w") as write_file:
    json.dump(sampleJson, write_file, indent=4, sort_keys=True)

# 

import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

data = json.loads(sampleJson)
print(data["company"]["employee"]["payble"]["salary"])

# Exercise 6: Convert the following Vehicle Object into JSON

import json
from json import JSONEncoder

class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price

class VehicleEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__

vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)

print("Encode Vehicle Object into JSON")
vehicleJson = json.dumps(vehicle, indent=4, cls=VehicleEncoder)
print(vehicleJson)

# Exercise 7: Convert the following JSON into Vehicle Object

import json

class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price

def vehicleDecoder(obj):
        return Vehicle(obj['name'], obj['engine'], obj['price'])

vehicleObj = json.loads('{ "name": "Toyota Rav4", "engine": "2.5L", "price": 32000 }',
           object_hook=vehicleDecoder)

print("Type of decoded object from JSON Data")
print(type(vehicleObj))
print("Vehicle Details")
print(vehicleObj.name, vehicleObj.engine, vehicleObj.price)

# Exercise 8: Check whether following json is valid or invalid. If Invalid correct it

import json

def validateJSON(jsonData):
    try:
        json.loads(jsonData)
    except ValueError as err:
        return False
    return True

InvalidJsonData = """{ "company":{ "employee":{ "name":"emma", "payble":{ "salary":7000 "bonus":800} } } }"""
isValid = validateJSON(InvalidJsonData)

print("Given JSON string is Valid", isValid)

# Exercise 9: Parse the following JSON to get all the values of a key ‘name’ within an array

import json

sampleJson = """[ 
   { 
      "id":1,
      "name":"name1",
      "color":[ 
         "red",
         "green"
      ]
   },
   { 
      "id":2,
      "name":"name2",
      "color":[ 
         "pink",
         "yellow"
      ]
   }
]"""

data = []
try:
    data = json.loads(sampleJson)
except Exception as e:
    print(e)

dataList = [item.get('name') for item in data]
print(dataList)
