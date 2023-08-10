import os
inputDir=r"./DirectoryContainingMyInputSample"
for file in os.scandir(inputDir):
    print(file.name)
    command="sudo docker run -v ~/DirectoryContainingMyInputSample:/DirectoryContainingMyInputSample -v ~/DirectoryInWhichToPutMyResults:/DirectoryInWhichToPutMyResults -v ~/DATABASE/hg38:/exceRpt_DB/hg38 -t rkitchen/excerpt INPUT_FILE_PATH=/DirectoryContainingMyInputSample/" + str(file.name)
    print(command)
    os.system(command)
