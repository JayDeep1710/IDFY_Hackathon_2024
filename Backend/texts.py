import glob
import os
# from docx import Document


labels = ["aadhar number" ,"Date of Birth","credit card Number","API Key","Bank Account Number","company", "booking number","age", "city", "country", "personally identifiable information", "driver licence", "person", "address", "email", "passport number", "Social Security Number", "phone number"]



def predict_entities_in_chunks(model, extracted_text, labels, chunk_size=200):
    words = extracted_text.split()
    results = []
    for i in range(0, len(words), chunk_size):
        chunk = ' '.join(words[i:i + chunk_size])
        entities = model.predict_entities(chunk, labels)
        results.append(entities)
    return results


def format_results(results):
    d = {}
    for entities in results:
        for entity in entities:
            d[entity["text"]] = entity["label"]
    return d



def process_text(text, model):
    path_to_data = {}
    result = predict_entities_in_chunks(model,text,labels,chunk_size=200)
    # result = model.predict_entities(text, labels)
    d = format_results(result)
    path_to_data["text"] = d
    return path_to_data


#Read text files
def read_text(model):
    folder_path = 'Testing/text_files'
    txt_files = glob.glob(os.path.join(folder_path, "*.txt"))
    text = ""
    path_to_data = {}
    for txt_file in txt_files:
        with open(txt_file, 'r') as file:
            text = file.read()
            result = predict_entities_in_chunks(model,text,labels,chunk_size=200)
            d = format_results(result)
            path_to_data[txt_file] = d
    return path_to_data


#Read Docx files
# def read_docx(folder_path):
#     doc_files = glob.glob(os.path.join(folder_path, "*.docx"))  # Find all .docx files
#     text = ""
    
#     for doc_file in doc_files:
#         # Open and read the .docx file
#         doc = Document(doc_file)
#         for para in doc.paragraphs:
#             text += para.text + "\n"  # Append each paragraph's text to the text variable with a newline
    
#     return text


