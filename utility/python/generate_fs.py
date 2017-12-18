#! /usr/bin/python3
import os
import refocus
import argparse

def generate_focal_stack(in_dir, out_dir, calib_mat):
    files = [f for f in os.listdir(in_dir) if 
                os.path.isfile(os.path.join(in_dir, f)) and 
                os.path.splitext(f)[-1].lower() == ".npy"]

    for f in files:
        #Create one outut folder for each focal stack
        focal_stack_folder = os.path.join(out_dir, os.path.splitext(f)[0])
        if not os.path.exists(focal_stack_folder):
            os.makedirs(focal_stack_folder)

        refocus.refocus(f, calib_mat, focal_stack_folder)

if __name__ == "__main__":
    #Add command line parser arguments
    parser = argparse.ArgumentParser(description='Create focal stacks from dataset.')
    parser.add_argument('datasetfolder', help='folder that contains the dataset to be converted to focal stacks')
    parser.add_argument('outdir', help='folder to save the focal stacks to. One folder per lightfield image is created')
    parser.add_argument('--calibmat', default='../../caldata/lfcalib/IntParamLF.mat', help='Path to calibration file (default: ../../caldata/lfcalib/IntParamLF.mat)')

    #Parse arguments
    args = parser.parse_args()

    #Generate focal stacks
    generate_focal_stack(args.datasetfolder, args.outdir, args.calibmat)
