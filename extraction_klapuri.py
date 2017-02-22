import essentia
import os
import json
import csv
from essentia.standard import *
import music21 as mus
from essentia import pool
import numpy as np
import matplotlib.pyplot as plt

def fetchFiles(inputDir, descExt=".json"):
    files = []
    for path, dname, fnames  in os.walk(inputDir):
        for fname in fnames:
            if descExt in fname.lower():
                files.append((path, fname))
    return files

def klapuri_extractor(inp, name, out):
	loader = essentia.standard.MonoLoader(filename = inp)
	audio = loader()
	multip = MultiPitchKlapuri(frameSize=8192, hopSize=441, minFrequency=20, maxFrequency=4500)
	f0vec = multip(audio)
	f0_names = out + name + '.f0s'
	print 'Writing results to: ' + f0_names
	write_f0s(f0_names, f0vec)

def write_f0s(filename, f0vec):
	time = 0
	f = open(filename, 'w')
	for f0 in f0vec:
		f.write(str(time) + "\t")
		for f0s in f0:
			f.write(str(f0s) + "\t")
		f.write("\n")
		time += 0.01
	f.close()

def main():
	filenames = fetchFiles(os.getcwd() + '/Dataset/maps', '.wav')
	out = 'evaluation/Maps_klapuri/'
	for path, fname in filenames:
		print "Extracting " + fname
		file_location = path + "/" + fname
		file_name, extension = os.path.splitext(fname)
		klapuri_extractor(file_location, file_name, out)
  

if __name__ == "__main__":
    main()