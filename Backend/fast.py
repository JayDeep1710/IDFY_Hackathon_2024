from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
import boto3
import botocore
from utils import *
from code_text import * 
from texts import *
from vision import *
from score import *
from fastapi.middleware.cors import CORSMiddleware
import sqlalchemy
import pandas as pd
from risk_score import *
# import psycopg2
suppress_output()
model = GLiNER.from_pretrained("urchade/gliner_mediumv2.1")
restore_output()

app = FastAPI()

origins = [
    "http://localhost:3000",
    # Add other origins if needed, such as deployed URLs
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

class DownloadRequest(BaseModel):
    bucket_name: str
    download_dir: str
    aws_access_key_id: str
    aws_secret_access_key: str
    aws_region: str
    
data =[]
@app.post("/local_folder")
def get_model(folder_path):
    d = {}
    copy_files_by_extension(folder_path)
    text_folder = "Testing/text_files"
    image_folder = "Testing/image_files"
    count = count_images_in_folder(image_folder)
    code_folder = "Testing/code_files"
    extracted_text1 = read_text(model)
    extracted_text2 = read_json(model)
    extracted_text3={}
    if count>0:
        extracted_text3 = stats(image_folder)
    data_vol=""
    if(len(extracted_text1)<=1):
        data_vol="small"
    elif(len(extracted_text1)==2):
        data_vol="medium"
    else :
        data_vol="large"
    
    d['texts'] = extracted_text1
    d['code'] = extracted_text2
    d['images'] = dict(extracted_text3)
    #changes here
    d["score"] = calculate_risk_score(d)
    return d


@app.post("/aws")
def download_all_objects(bucket_name, aws_access_key_id, aws_secret_access_key, aws_region):
    # Initialize S3 resource with the provided credentials
    download_dir = "AWS_bucket"
    s3 = boto3.resource(
        's3',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=aws_region
    )

    my_bucket = s3.Bucket(bucket_name)
    for s3_object in my_bucket.objects.all():
        key = s3_object.key
        path, filename = os.path.split(key)
        local_file_path = os.path.join(download_dir, key)
        if not os.path.exists(os.path.dirname(local_file_path)):
            os.makedirs(os.path.dirname(local_file_path))
        if filename:
            try:
                my_bucket.download_file(key, local_file_path)
                print(f"Downloaded {key} to {local_file_path}")
            except botocore.exceptions.ClientError as e:
                print(f"Failed to download {key}: {e}")
        else:
            print(f"Skipping directory {key}")
    results =  get_model(download_dir)
    return results

@app.post("/text")
def analyze_text(text):
    result = process_text(text, model)
    d = result['text']
    d2 = {}
    d2["documents"] = d
    data = {}
    data["texts"] = d2
    data["code"] = {}
    data["images"] = {}
    temp=data
    temp["score"]=calculate_risk_score(data)
    return temp

    
# @app.post("sql")
# def get_database_as_text(host, dbname, user, password, query):
#     try:
#         connection = psycopg2.connect(
#             host=host,
#             dbname=dbname,
#             user=user,
#             password=password
#         )
#         cursor = connection.cursor()
#         cursor.execute(query)
#         rows = cursor.fetchall()
#         result = "\n".join([str(row) for row in rows])
#         cursor.close()
#         connection.close()
#         d = process_text(result, model)
#         data_vol=""
#         if(len(d)<=1):
#             data_vol="small"
#         elif(len(d)==2):
#             data_vol="medium"
#         else :
#             data_vol="large"
#         d["score"] = calculate_risk_score(data,data_vol)
#         return d

    # except Exception as e:
    #     return f"An error occurred: {e}"
@app.post("/sql")   
def get_database_as_text(host,dbname,user,password):
    print("Analyze PII route called")
    mysql_table="documents"
    mysql = host.split(":")
    mysql_host = mysql[0]
    mysql_port = mysql[1]
    # Check if MySQL credentials are provided
    engine = sqlalchemy.create_engine(f'mysql+pymysql://{user}:divy123%40@{mysql_host}:{mysql_port}/{dbname}')
    conn = engine.connect()
    df = pd.read_sql_table(mysql_table, conn)
    text = df.to_string()
    print("Data from MySQL table read successfully. Processing...")

    result = process_text(text,model)
    d = result['text']
    d2 = {}
    d2["documents"] = d
    data = {}
    data["texts"] = d2
    data["code"] = {}
    data["images"] = {}
    temp=data
    temp["score"]=calculate_risk_score(data)
    return temp