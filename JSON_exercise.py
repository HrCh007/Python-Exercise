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
