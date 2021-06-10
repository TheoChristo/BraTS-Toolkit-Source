import os
import datetime

from brats_toolkit.segmentor import Segmentor


# log
starttime = str(datetime.datetime.now().time())
print("*** starting at", starttime, "***")

# instantiate
# seg = Segmentor(verbose=True)
seg = Segmentor(config='brats_toolkit/config/dockers_small20.json', verbose=True, gpu='2')
# input files
# t1File = "test/t1.nii.gz"
# t1cFile = "test/t1c.nii.gz"
# t2File = "test/t2.nii.gz"
# flaFile = "test/fla.nii.gz"
t1File = "TestData/segmentor_input/TCGA-DU-7294_hdbet_brats_t1.nii.gz"
t1cFile = "TestData/segmentor_input/TCGA-DU-7294_hdbet_brats_t1c.nii.gz"
t2File = "TestData/segmentor_input/TCGA-DU-7294_hdbet_brats_t2.nii.gz"
flaFile = "TestData/segmentor_input/TCGA-DU-7294_hdbet_brats_fla.nii.gz"

# output
outputFolder = "TestData/segmentor_output/"

# algorithms we want to select for segmentation
cids = ['mic-dkfz', 'scan', 'xfeng', 'lfb_rwth', 'zyx_2019', 'scan_2019']
cid = 'sanet0-20'
# execute it
# for cid in cids:
try:
    outputFile = outputFolder + cid + ".nii.gz"
    seg.segment(t1=t1File, t2=t2File, t1c=t1cFile, fla=flaFile, cid=cid, outputPath=outputFile)

except Exception as e:
    print("error:", str(e))
    print("error occured for:", cid)

# log
endtime = str(datetime.datetime.now().time())
print("*** finished at:", endtime, "***")