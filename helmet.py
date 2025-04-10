import cv2
import numpy as np
import os
import imutils
from tensorflow.keras.models import load_model
# import easyocr
import os 
import subprocess
import glob
import utils
import os
import shutil

def remove_all_subdirectories(parent_dir):
    # List all entries in the directory
    for entry in os.listdir(parent_dir):
        # Construct full path to the entry
        entry_path = os.path.join(parent_dir, entry)
        # Check if the entry is a directory
        if os.path.isdir(entry_path):
            # Remove the directory and all its contents
            shutil.rmtree(entry_path)
            print(f"Removed: {entry_path}")



def detect_plates(video_path, selected_location):
    parent_directory = os.path.join('./yolov5/runs/detect/')
    remove_all_subdirectories(parent_directory)

    command = [
        'python', './yolov5/detect_v2.py',
        '--weights', './yolov5/best.pt',
        '--img', '416',
        '--conf', '0.5',
        '--source', video_path,
        '--view-img',
        '--save-txt',
        '--save-crop'

    ]
    mdl = utils.load_pkl_model()
    ret = mdl(video_path)

    subprocess.run(command)

    print('Detection Complete')

    return utils.make_doc(ret)


# detect_plates(r"C:\Users\SURYA S\210623\TrafficManagement\TrafficManagement\t1.mp4")
