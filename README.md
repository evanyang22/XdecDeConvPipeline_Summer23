# XdecDeConvPipeline_Summer23

Preliminary Excerpt aligner
Copy and paste the autoaligner into terminal Python3 to run it

This one works


sudo docker run -v ~/DirectoryContainingMyInputSample:/exceRptInput -v ~/DirectoryInWhichToPutMyResults:/exceRptOutput -v ~/database/hg38:/exceRpt_DB/hg38 -t rkitchen/excerpt INPUT_FILE_PATH=/exceRptInput/SRR026761.sra


This script works:

import os
inputDir=r"./exceRptInput"
for file in os.scandir(inputDir):
    print(file.name)
    command="sudo docker run -v ~/DirectoryContainingMyInputSample:/exceRptInput -v ~/DirectoryInWhichToPutMyResults:/exceRptOutput -v ~/DATABASE/hg38:/exceRpt_DB/hg38 -t rkitchen/excerpt INPUT_FILE_PATH=/exceRptInput/" + str(file.name)
    print(command)
    os.system(command)
