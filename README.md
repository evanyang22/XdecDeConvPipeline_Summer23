# XdecDeConvPipeline_Summer23

Preliminary Excerpt aligner
import os
inputDir=r"./input"
for file in os.scandir(inputDir):
	print(file.name)
	command="sudo docker run -v ~/DirectoryContainingMyInputSample:/input -v ~/DirectoryInWhichToPutMyResults:/exceRptOutput -v ~/DATABASE/hg38:/exceRpt_DB/hg38 -t rkitchen/excerpt INPUT_FILE_PATH=/input/" + str(file.name)
	print(command)
	os.system(command)
