from sklearn import metrics
import numpy as np
import csv
import os



#precision_recall_fscore_support(y_true, y_pred, average='micro')


def compare(y_pred, y, threshold):
	score = 0
	for f in y:
		for k, ff in enumerate(y_pred):
			diff = abs(float(ff) - float(f))
			if diff < float(f)*threshold:
				score += 1
				y_pred.pop(k)
	return score

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
		b = np.array(filter (lambda a: a!= 0.0, line[1:]))
		results_kla.append(filter (lambda a: a!= '', b))

	score = 0
	prec = 0
	rec = 0
	for k, frame in enumerate(results_GT):
		rec += len(frame)
		try:
			score += compare(frame, results_kla[k], 0.03)
			prec += len(results_kla[k])
		except:
			pass
	print "Number of correct predicted:\t%i" % (score)	
	print "Number of predicted:\t\t%i" % (prec)
	print "Number of Ground Truth:\t\t%i" % (rec)
	print "Precision:\t\t\t%.4f" % (score/float(prec) if prec else 0)
	print "Recall:\t\t\t\t%.4f" % (score/float(rec) if rec else 0)	

	return score, prec, rec

def main():
	filenames = fetchFiles('Saarland', '.f0s')
	score = 0
	prec = 0
	rec = 0
	for path, fname in filenames:
		print "Evaluating " + fname
		GT_location = path + "/" + fname
		klapuri_location = 'Saarland_klapuri/' + fname
		s,p,r= evaluate(GT_location, klapuri_location)
		score +=s
		prec +=p
		rec += r

	print "******************************************"
	print "Number of correct predicted:\t%i" % (score)	
	print "Number of predicted:\t\t%i" % (prec)
	print "Number of Ground Truth:\t\t%i" % (rec)
	print "Precision:\t\t\t%.4f" % (score/float(prec) if prec else 0)
	print "Recall:\t\t\t\t%.4f" % (score/float(rec) if rec else 0)	


if __name__ == "__main__":
    main()

