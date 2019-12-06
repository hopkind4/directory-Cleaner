import os
import shutil
from random import randint
root = r"/home/dthops/FileCleaner/Test Files"

path = root + r"/Collected Items"
os.mkdir(path)

folder = "level"
counter = 0

arr = (".csv",".jpg",".doc",".png",".txt",".pdf",".docx",".mp3",".ai",".psd",".py",".ppt",".pps",".pptx",".xls",".xlsx",".c")


for (root,dirs,files) in os.walk(root, topdown=True): 
    #print (root)
    rootCotainsPath = root.find(path)
    if(rootCotainsPath):
        for fileName in files: # for each file in the directory
            folderPath = path + r"/"+ fileName[fileName.find(".")+1:]
            folderExists = os.path.isdir(folderPath)
            if (fileName.endswith(arr))and(folderExists == False): #if the file ends in the correct extension
                os.mkdir(folderPath)
                shutil.move(root+ r"/"+ fileName,folderPath)
            elif(fileName.endswith(arr)):
                if(os.path.exists(folderPath+ r"/"+ fileName)): # if the file exists
                    tempName = fileName
                    num = 0
                    while(os.path.exists(folderPath+ r"/"+ tempName)):
                        tempName = fileName[:fileName.find(".")] + "("+str(num)+")" + fileName[fileName.find("."):]
                        print (tempName)
                        num += 1
                    shutil.move(root+ r"/"+ fileName,folderPath+ r"/"+tempName)
                else:
                    shutil.move(root+ r"/"+ fileName,folderPath)