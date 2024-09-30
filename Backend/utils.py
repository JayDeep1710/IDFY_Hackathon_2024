import os
import shutil
import glob
import sys
from gliner import GLiNER
import time
import threading
import json

import csv
from vision import *
from texts import *
from visualize import *
from code_text import *





# Define different file extensions for each category
doc_extensions = ['.txt','.doc', '.docx']
image_extensions = ['.jpg', '.jpeg', '.png', '.gif']
code_extensions = ['.py', '.js', '.java', '.cpp', '.html', '.css', '.json', '.yaml', '.yml']
labels = ["Date of Birth","credit card Number","API Key","Bank Account Number","aadhar number" ,"company", "booking number","age", "city", "country", "personally identifiable information", "driver licence", "person", "address", "email", "passport number", "Social Security Number", "phone number"]
        


# Function to suppress output
def suppress_output():
    sys.stdout = open(os.devnull, 'w')
    sys.stderr = open(os.devnull, 'w')

# Function to restore output
def restore_output():
    sys.stdout = sys.__stdout__
    sys.stderr = sys.__stderr__

def copy_files_by_extension(source_directory, doc_dest="Testing/text_files", image_dest="Testing/image_files", code_dest="Testing/code_files"):
    if not os.path.exists(source_directory):
        print("\033[31mDirectory not found!\033[0m")  # Print error in red
        return
    
    if not os.path.exists(doc_dest):
        os.makedirs(doc_dest)
    if not os.path.exists(image_dest):
        os.makedirs(image_dest)
    if not os.path.exists(code_dest):
        os.makedirs(code_dest)

    for root, dirs, files in os.walk(source_directory):
        for file in files:
            source_file_path = os.path.join(root, file)

            if file.endswith(tuple(doc_extensions)):
                shutil.copy(source_file_path, doc_dest)
                # print(f"Copied {file} to {doc_dest}")
            elif file.endswith(tuple(image_extensions)):
                shutil.copy(source_file_path, image_dest)
                # print(f"Copied {file} to {image_dest}")

            elif file.endswith(tuple(code_extensions)):
                shutil.copy(source_file_path, code_dest)







#convert CSV file to text to process
def csv_to_text(csv_file_path, output_file_path):
    # Open the CSV file
    with open(csv_file_path, mode='r') as csv_file:
        # Read the CSV file
        csv_reader = csv.reader(csv_file)
        
        # Open a text file to save the output
        with open(output_file_path, mode='w') as text_file:
            for row in csv_reader:
                # Join each row into a single string and write to the text file
                row_text = ' '.join(row)  # You can modify the delimiter here (e.g., space, comma)
                text_file.write(row_text + "\n")  # Write each row followed by a newline
                
def predict_entities_in_chunks(model, extracted_text, labels, chunk_size=200):

    words = extracted_text.split()

    results = []

    for i in range(0, len(words), chunk_size):
        chunk = ' '.join(words[i:i + chunk_size])
        entities = model.predict_entities(chunk, labels)
        results.append(entities)
    return results


    

def search(i,model):
    if i==1:
        ###
        print("\033[32m Loading model... \033[0m")
        suppress_output()
       
        restore_output()
        print("\033[32m Model Loaded Sucessfully! \033[0m")
        print("\033[32m Searching for Personally Identifiable Information in Text files \033[0m")
        ###Text extraction
        extracted_dict = read_text(model)
        for path, d in extracted_dict.items():
            file_name = path.split("/")[-1]
            print(f"In file \033[91m{file_name}\033[0m:")
            if len(d)>0:
                print_dict_in_color(d)
            else:
                print("\033[32mNo PII data found\033[0m")
                
    if i==6:
        
        print("\033[32m Loading model... \033[0m")
        suppress_output()
        model = GLiNER.from_pretrained("urchade/gliner_multi_pii-v1")
        restore_output()
        print("\033[32m Model Loaded Sucessfully! \033[0m")
        
        extracted_text = read_cpp()
        print(extracted_text)
        suppress_output()
        entities = model.predict_entities(extracted_text,  labels)
        restore_output()
        suppress_output()
        restore_output()
        for entity in entities:
            print(entity["text"], "=>", entity["label"])
            
    if i==5:
        d = stats("/Users/jaydeep/Desktop/IDFY_Hackathon_2024/Backend/Test")
        print(d)
    if i==7:
                ###
        print("\033[32m Loading model... \033[0m")
        print("\033[32m Model Loaded Sucessfully! \033[0m")
        print("\033[32m Searching for Personally Identifiable Information in Text files \033[0m")
        extracted_text = " "
        ###Text extraction
        extracted_text += read_text(model)
        ###JSON extraction
        extracted_text += read_json(model)
        #passing the text in chunk size of 200
        results = predict_entities_in_chunks(model, extracted_text, labels, chunk_size=50)
        d2 = stats("/Users/jaydeep/Desktop/IDFY_Hackathon_2024/Backend/Test")
        d = format_results(results)
        print_dict_in_color(d)
        print_dict_in_color(d2)
        
        
            
            

            
        
        
