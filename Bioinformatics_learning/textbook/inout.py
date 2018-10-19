import sys
import os

infilename = os.path.expanduser("E:\\dataset_205_5.txt")
outfilename = os.path.expanduser("E:\\1.txt")

def readlines(filename):
	with open(os.path.expanduser(filename), 'r') as infile:
		return infile.readlines()

def writelines(filename, outstr):
	with open(filename, 'w') as outfile:
		outfile.write(outstr)

def output(outstr):
	writelines(outfilename, outstr)
	
infilelines = readlines(infilename)
