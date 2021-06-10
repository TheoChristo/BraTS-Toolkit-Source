import os
# from path import Path
import os.path as Path
from brats_toolkit.preprocessor import Preprocessor
import sys

def batch_test():
    print ("Running Batch Pre-Processor Test")
    # define inputs and outputs
    inputDir = "./TestData/input_preprocessor_batch_processing/exams_to_preprocess/"
    outputDir = "./TestData/output_preprocessor_batch/"

    # execute it
    prep.batch_preprocess(exam_import_folder=inputDir,
                      exam_export_folder=outputDir, mode="gpu", confirm=True, skipUpdate=False, gpuid='3')

def single_test():
    print ("Running Single Pre-Processor Test")
    examName = "TCGA-DU-7294"
    t1File = "TestData/input_preprocessor_single_processing/TCGA-DU-7294/TCGA-DU-7294-T1.nii.gz"
    t1cFile = "TestData/input_preprocessor_single_processing/TCGA-DU-7294/TCGA-DU-7294-T1c.nii.gz"
    t2File = "TestData/input_preprocessor_single_processing/TCGA-DU-7294/TCGA-DU-7294-T2.nii.gz"
    flaFile = "TestData/input_preprocessor_single_processing/TCGA-DU-7294/TCGA-DU-7294-FLAIR.nii.gz"

    # define outputs
    outputDir = "TestData/output_preprocessor_single/TCGA-DU-7294"

    # execute it
    prep.single_preprocess(t1File=t1File, t1cFile=t1cFile, t2File=t2File, flaFile=flaFile,
                        outputFolder=outputDir, mode="gpu", confirm=True, skipUpdate=False, gpuid='3')

# instantiate
prep = Preprocessor()
single_test()
# batch_test()
sys.exit(0)
