# File to format and get images from external SD card

import os, sys, time

filepath = "/home/pi/images/"
sys.path.insert(0,filepath)

def getImagePath(base_directory,filename):

    for root, _, files in os.walk(base_directory):
        for file in files:
            if file == filename:
                return os.path.join(root, file)
    return None


def getListImageandPath(base_directory):
    file_names = []
    file_paths = []
    
    for root, _, files in os.walk(base_directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_names.append(file)
            file_paths.append(file_path)
    
    return file_names, file_paths

#print(getListImageandPath("/home/pi/images/"))