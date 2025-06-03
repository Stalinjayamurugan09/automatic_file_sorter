# Automate File Sorter in File Explorer

import os,shutil

path = "C:/Users/stali/OneDrive/Pictures/Python Tutorial/"

folder_names = ['csv files', 'image files', 'text files']

for folder in range(len(folder_names)):
    folder_already_exist = os.path.exists(path + folder_names[folder])
    if not folder_already_exist:
        # os.makedirs(path_to_create_directory)
        os.makedirs(path + folder_names[folder])

for file in os.listdir(path):
    if ".csv" in file and not os.path.exists(path + "csv files/" + file):
        # shutil.move(from_path,to_path)
        shutil.move(path + file,path + "csv files/" + file)
    elif ".png" in file and not os.path.exists(path + "/" + "image files/" + file):
        shutil.move(path + file,path + "image files/" + file)
    elif ".txt" in file and not os.path.exists(path + "/" +"text files/" + file):
        shutil.move(path + file,path + "text files/" + file)