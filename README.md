# XdecDeConvPipeline_Summer23

Preliminary Excerpt aligner
Copy and paste the autoaligner into terminal Python3 to run it

This one works


sudo docker run -v ~/DirectoryContainingMyInputSample:/exceRptInput -v ~/DirectoryInWhichToPutMyResults:/exceRptOutput -v ~/database/hg38:/exceRpt_DB/hg38 -t rkitchen/excerpt INPUT_FILE_PATH=/exceRptInput/SRR026761.sra
