import os
inputDir=r"./input"
for file in os.scandir(inputDir):
    print(file.name)
    command="sudo docker run -v ~/input:/exceRptInput -v ~/output:/exceRptOutput -v ~/DATABASE/hg38:/exceRpt_DB/hg38 -t rkitchen/excerpt INPUT_FILE_PATH=/input/" + str(file.name)
    print(command)
    os.system(command)
