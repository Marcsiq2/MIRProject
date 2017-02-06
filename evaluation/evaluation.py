from sklearn import metrics
import numpy as np
import csv
import os



#precision_recall_fscore_support(y_true, y_pred, average='micro')


def fetchFiles(inputDir, descExt=".json"):
    files = []
    for path, dname, fnames  in os.walk(inputDir):
        for fname in fnames:
            if descExt in fname.lower():
                files.append((path, fname))
    return files

def evaluate(file_location, klapuri_location):
	with open(file_location) as f:
		reader = np.loadtxt(f, delimiter = "\t")
	results_GT = []
	for line in reader:
		results_GT.append(filter (lambda a: a!= 0.0, line[1:]))

	with open(klapuri_location) as f:
		reader_kla = csv.reader(f, delimiter = "\t")
		d = list(reader_kla)
	results_kla = []
	for line in d:
		b = filter (lambda a: a!= 0.0, line[1:])
		results_kla.append(filter (lambda a: a!= '', b))

	print metrics.accuracy_score(results_GT, results_kla)



def main():
	filenames = fetchFiles('Saarland', '.f0s')
	for path, fname in filenames:
		print "Evaluating " + fname
		GT_location = path + "/" + fname
		klapuri_location = 'Saarland_klapuri/' + fname
		evaluate(GT_location, klapuri_location)
		

if __name__ == "__main__":
    main()