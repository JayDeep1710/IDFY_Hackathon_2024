import json
import os
import glob
import random
def get_score():
    return random.randint(1,100)

labels = ["Date of Birth","credit card Number","API Key","Bank Account Number","aadhar number" ,"company", "booking number","age", "city", "country", "personally identifiable information", "driver licence", "person", "address", "email", "passport number", "Social Security Number", "phone number"]


def format_json(entities):
    d = {}
    for entity in entities:
        d[entity["text"]] = entity["label"]
    return d

def read_json(model):
    folder_path = 'Testing/code_files'
    path_to_data = {}
    json_files = glob.glob(os.path.join(folder_path, "*.json"))
    for json_file in json_files:
        with open(json_file, "r") as json_file2:
            data = json.load(json_file2)
            text = json.dumps(data, indent=4)
            result = model.predict_entities(text, labels)
            p = json_file.split('/')[-1]
            d = format_json(result)
            path_to_data[p] = d
    return path_to_data

#read CPP
def read_cpp(folder_path):
    cpp_files = glob.glob(os.path.join(folder_path, "*.cpp"))
    text = ""
    
    for cpp_file in cpp_files:
        with open(cpp_file, "r") as file:
            cpp_code = file.read()
            text += cpp_code + "\n"
    return text


#Read Python
def read_python(folder_path):
    cpp_files = glob.glob(os.path.join(folder_path, "*.py"))
    text = ""
    
    for cpp_file in cpp_files:
        with open(cpp_file, "r") as file:
            cpp_code = file.read() 
            text += cpp_code + "\n"  
    return text


#Read Java
def read_java(folder_path):
    cpp_files = glob.glob(os.path.join(folder_path, "*.java"))
    text = ""
    
    for cpp_file in cpp_files:
        with open(cpp_file, "r") as file:
            cpp_code = file.read()
            text += cpp_code + "\n"
    return text