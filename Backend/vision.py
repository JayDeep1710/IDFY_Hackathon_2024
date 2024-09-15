from collections import defaultdict
from PIL import Image
from ultralytics import YOLO
from utils import *
from visualize import *
import os


model = YOLO("train3-1/weights/best.pt")
names = {0: 'aadhar', 1: 'dl', 2: 'pan', 3: 'passport', 4: 'utility', 5: 'voterid'}


def count_images_in_folder(folder_path):
    image_extensions = ('.png', '.jpg', '.jpeg')
    count = 0
    for file_name in os.listdir(folder_path):
        if file_name.lower().endswith(image_extensions):
            try:
                img = Image.open(os.path.join(folder_path, file_name))
                img.verify()
                count += 1
            except (IOError, SyntaxError) as e:
                pass
    return count


def stats(path):
    """
    path : str
    return : stats (default dict)
    """
    dict = defaultdict(int)  
    results = model(path,verbose=False)
    for result in results:
        detections = result.boxes.cls.tolist()
        for detetction in detections:
            id = int(detetction)
            label = names[id]
            dict[label]+=1
    dict["PII intentified images"] = sum(dict.values())
    return dict

