import time
from utils import *
from gliner import GLiNER
import os
import os
import boto3
import botocore
import sqlalchemy
import pandas as pd
from utils import *
from code_text import * 
from texts import *
from vision import *
from score import *
from risk_score import *


text = """
\033[92m                                                                     
                                                                     
\033[31mIIIIIIIII\033[92mDDDDDDDDDDDDD     \033[31mFFFFFFFFFFFFFFFFFFFFF\033[92mYYYYYYY       YYYYYYY
\033[31mI:::::::I\033[92mD::::::::::::DDD  \033[31mF:::::::::::::::::::F\033[92mY:::::Y       Y:::::Y
\033[31mI:::::::I\033[92mD:::::::::::::::DD\033[31mF:::::::::::::::::::F\033[92mY:::::Y       Y:::::Y
\033[31mII::::::I\033[92mDDD:::::DDDDD:::::FF\033[31m::::::FFFFFFFFF:::F\033[92mY::::::Y     Y::::::Y
  \033[31mI::::I   \033[92mD:::::D    D:::::D\033[31mF:::::F       \033[31mFFFFF\033[92mYYY:::::Y   Y:::::YYY
  \033[31mI::::I   \033[92mD:::::D     D:::::\033[31mF:::::F               \033[92mY:::::Y Y:::::Y   
  \033[31mI::::I   \033[92mD:::::D     D:::::\033[31mF::::::FFFFFFFFFF\033[92m      Y:::::Y:::::Y    
  \033[31mI::::I   \033[92mD:::::D     D:::::\033[31mF:::::::::::::::F\033[92m       Y:::::::::Y     
  \033[31mI::::I   \033[92mD:::::D     D:::::\033[31mF:::::::::::::::F\033[92m        Y:::::::Y      
  \033[31mI::::I   \033[92mD:::::D     D:::::\033[31mF::::::FFFFFFFFFF\033[92m         Y:::::Y       
  \033[31mI::::I   \033[92mD:::::D     D:::::\033[31mF:::::F\033[92m                   Y:::::Y       
  \033[31mI::::I   \033[92mD:::::D    D:::::D\033[31mF:::::F\033[92m                   Y:::::Y       
\033[31mII::::::I\033[92mDDD:::::DDDDD:::::FF\033[31m:::::::FF\033[92m                 Y:::::Y       
\033[31mI:::::::I\033[92mD:::::::::::::::DD\033[31mF::::::::FF\033[92m              YYYY:::::YYYY    
\033[31mI:::::::I\033[92mD::::::::::::DDD  \033[31mF::::::::FF\033[92m              Y:::::::::::Y    
\033[31mIIIIIIII\033[92mDDDDDDDDDDDDD      \033[31mFFFFFFFFFFF\033[92m              YYYYYYYYYYYYY                                          
                                                                     
                                                                     \033[0m
"""
d = {1:"Texts", 2:"Docs", 3:"Pdfs" ,4:"CSV", 5:"Images", 6:"Codes", 7:"All"}
# Split the text into lines
lines = text.splitlines()
suppress_output()
model = GLiNER.from_pretrained("urchade/gliner_multi_pii-v1")
restore_output()
# Loop through each line and print it with a delay
for line in lines:
    print(line)
    time.sleep(0.1)  # Adjust the delay (in seconds) as needed
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

def download_all_objects(bucket_name, aws_access_key_id, aws_secret_access_key, aws_region):
    download_dir = "/Users/jaydeep/Desktop/IDFY_Hackathon_2024/Backend/AWS_bucket"
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
        print("Bucket Downloaded")
    results =  get_model(download_dir)
    return results

def print_columns(d, indent=0):
    for key, value in d.items():
        if isinstance(value, dict) or isinstance(value, defaultdict):
            print(f"\033[32m{' ' * indent}{key}:\033[0m")
            print_columns(value, indent + 4)
        else:
            # Color keys in green and values in red
            print(f"\033[32m{' ' * indent}{key:<40}\033[0m \033[31m{value:<30}\033[0m")

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
    print(result)
    d = result['text']
    d2 = {}
    d2["documents"] = d
    data = {}
    data["texts"] = d2
    data["code"] = {}
    data["images"] = {}
    # temp=data
    # temp["score"]=calculate_risk_score(data)
    return data
while True:
    print("\033[92m" + "=" * 100 + "\033[0m")

    print("\033[32m 1. Search Database \033[0m")
    print("\033[32m 2. Search Local Folder \033[0m")
    print("\033[32m 3. Search Cloud storage \033[0m")
    print("\033[32m 4. Exit \033[0m")
    # ANSI escape code for green text
    print("\033[92m" + "=" * 100 + "\033[0m")

    i = input()
    if i=="1":
        print("\033[32mEnter the host_name\033[0m")
        a = input()
        print("\033[32mEnter the db_name\033[0m")
        b = input()
        print("\033[32mEnter the user\033[0m")
        c = input()
        print("\033[32mEnter the password\033[0m")
        d = input()
        res = get_database_as_text(a,b,c,d)
        print_columns(res)
    elif i=="2":
        print("\033[32mEnter the path to the local folder\033[0m")
        path = input()
        copy_files_by_extension(path)
        print("\033[32mSearching...\033[0m")
        search(1,model)
        
    elif i=="3":
        print("\033[32mEnter the bucket_name\033[0m")
        a = input()
        print("\033[32mEnter the aws_access_key_id\033[0m")
        b = input()
        print("\033[32mEnter the aws_secret_access_key\033[0m")
        c = input()
        print("\033[32mEnter the aws_region\033[0m")
        d = input()
        result=download_all_objects(a,b,c,d)
        print_columns(result)
        d2 = stats("/Users/jaydeep/Desktop/IDFY_Hackathon_2024/Backend/Test")
        print_dict_in_color(d2)
    elif i=="4":
        print("\033[32mEnter the bucket_name\033[0m")
        a = input()
        d = process_text(a,model)
        print(d)
    elif i=="5":
        break
        
    else:
        print(f"\033[32m{i} is not a valid input \033[0m")
    