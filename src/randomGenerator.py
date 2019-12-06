import os
from random import randint
root = r"/home/dthops/FileCleaner/Test Files"

height = 4
width = 3 

folder = "level"
path = root
counter = 0
fileNum = 0

arr = [".csv",".jpg",".doc",".png",".txt",".pdf",".docx",".mp3",".ai",".psd",".py",".ppt",".pps",".pptx",".xls",".xlsx"]


print("here")
def buildDir(count,path):
    count = count+1
    dirCount = randint(0,width)#random number of dirs for current folder
    filCount = randint(0,width)#random number of files
    for ii in range(0,dirCount):
        extension = randint(0,len(arr)-1)
        extension =  arr[extension]
        fileNum= randint(0,1000000)
        file = open(path + r"/" +"File"+str(fileNum)+extension,"w")
        
        print(path)
        tempFolder = folder+str(count)+"-"+str(ii)
        tempPath = path+ r"/" + tempFolder
        os.mkdir(tempPath)
        print(tempPath)

        if(count < 5):
            buildDir(count,tempPath)

buildDir(counter,root)

