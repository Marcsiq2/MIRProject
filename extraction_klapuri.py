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

def klapuri_extractor(inp, name):
	loader = essentia.standard.MonoLoader(filename = inp)
	audio = loader()
	multip = MultiPitchKlapuri(frameSize=4096, hopSize=441)
	f0vec = multip(audio)
	time = 0
	f0_names = 'evaluation/Saarland_klapuri/' + name + '.f0s'
	print 'Writing results to: ' + f0_names

	f = open(f0_names, 'w')
	for f0 in f0vec:
		f.write(str(time) + "\t")
		for f0s in f0:
			f.write(str(f0s) + "\t")
		f.write("\n")
		time += 0.01



def main():
	filenames = fetchFiles(os.getcwd() + '/Dataset/Saarland', '.mp3')
	for path, fname in filenames:
		print "Extracting " + fname
		file_location = path + "/" + fname
		file_name, extension = os.path.splitext(fname)
		klapuri_extractor(file_location, file_name)
  

if __name__ == "__main__":
    main()