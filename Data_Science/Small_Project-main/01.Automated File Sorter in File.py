import os, shutil
path=("C:/Users/Admin/Downloads/New folder")
file_names =os.listdir(path)
folder_names= ['csv files', 'imgage files','text files']
for loop in range (0,2):
    if not os.path.exists(path + folder_names[loop]):
        os.makedirs(path + folder_names[loop])
for file in file_names:
    if '.JPG' in file and not os.path.exists(path + "image file/"+ file):
        shutil.move(path + file, path + "image file/"+ file)    
    else: 
        print('There are file in this path that were not moved!')
