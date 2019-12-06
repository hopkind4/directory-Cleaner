import os
import shutil
from random import randint
root = r"/home/dthops/FileCleaner/Test Files"

folder = "level"
path = root
counter = 0

arr = (".csv",".jpg",".doc",".png",".txt",".pdf",".docx",".mp3",".ai",".psd",".py",".ppt",".pps",".pptx",".xls",".xlsx")


for (root,dirs,files) in os.walk(path, topdown=True): 
    #print (root)
    for fileName in files: # for each file in the directory
        folderPath = path + r"/"+ fileName[fileName.find(".")+1:]
        folderExists = os.path.isdir(folderPath)
        if (fileName.endswith(arr))and(folderExists == False): #if the file ends in the correct extension
            os.mkdir(folderPath)
            shutil.move(root+ r"/"+ fileName,folderPath)
        elif(fileName.endswith(arr)):
            shutil.move(root+ r"/"+ fileName,folderPath)

    #print (dirs) 
    #print (files) 

