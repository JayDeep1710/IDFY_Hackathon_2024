import sqlalchemy
import pandas as pd
from texts import *
from gliner import GLiNER
model = GLiNER.from_pretrained("urchade/gliner_mediumv2.1")
def get_database_as_text(host,dbname,user,password):
    print("Analyze PII route called")
    mysql_table="documents"
    mysql = host.split(":")
    mysql_host = mysql[0]
    mysql_port = mysql[1]
    # Check if MySQL credentials are provided
    if host and dbname and user and password:
        engine = sqlalchemy.create_engine('mysql+pymysql://root:divy123%40@127.0.0.1:3306/idfy')
        print(f"mysql+pymysql://{user}:{password}@{mysql_host}:{mysql_port}/{dbname}")
        conn = engine.connect()
        df = pd.read_sql_table(mysql_table, conn)
        text = df.to_string()
        print("Data from MySQL table read successfully. Processing...")
    else:
        print("Incomplete MySQL credentials provided.")
    result = process_text(text,model)
    d = result['text']
    d2 = {}
    d2["documents"] = d
    data = {}
    data["score"] = 48
    data["texts"] = d2
    data["code"] = {}
    data["images"] = {}
    return data

# Sample values for the MySQL connection
mysql = '127.0.0.1:3306'
mysql_port = '3306'
mysql_user = 'root'
mysql_password = 'divy123%40'
mysql_database = 'idfy'
mysql_table = 'documents'
ans=get_database_as_text(mysql,mysql_database,mysql_user,mysql_password)
print(ans)
