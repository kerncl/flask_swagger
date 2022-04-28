from datetime import datetime
from flask import request
import json

sample_data = [{'Test1': {'Data': 'Information1'}},
               {'Test2': {'Data': 'Information2'}},
               {'Test3': {'Data': 'Information3'}}]


def TestApi():
    return {'Message': "successful",
            'Time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}


def getAll():
    return [data for data in sample_data]


def postdata():
    data = request.json
    if data in [key for key in sample_data]:
        return {"Message": f"{data.keys()} already exists in our database"}, 400
    sample_data.append(data)
    return {"Message": "Successful"}, 201


def getTestname(testname: str):
    for key in sample_data:
        if testname in key:
            return key, 200
    return {'Message': f'{testname} not found in testname'}, 404


def postTestname(testname: str):
    for key in sample_data:
        if testname in key:
            return {'Message': f"{testname} already exists in database"}, 404
    data = request.json
    new_data = {testname: data}
    sample_data.append(new_data)
    return new_data, 200


def putTestname(testname: str):
    data = request.json
    for key in sample_data:
        if testname in key:
            new_data = {testname: data}
            return new_data, 200
    new_data = {testname: data}
    sample_data.append(new_data)
    return new_data, 200


def deleteTestname(testname: str):
    for key in sample_data:
        if testname in key:
            sample_data.remove(key)
            return {"Message": f"Successfully Deleted {key}"}, 200
    return {"Message": f"{testname} not found in database"}, 404


def dummy(testname: str):
    return {"Message": "Not longer support"}, 200


def getJsonfile():
    args = request.files
    file = args['jsonfile']
    if not file.filename.endswith('json'):
        return {"Message": "Only Accept Json File"}, 404
    json_str = bytes.decode(file.stream.read())
    json_dict = json.loads(json_str)
    return json_dict, 200
