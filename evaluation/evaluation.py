from sklearn import metrics
import numpy as np
import csv
import os



#precision_recall_fscore_support(y_true, y_pred, average='micro')


def compare(y_pred, y, threshold):
	yy = y_pred
	score = 0
	for f in y:
		for k, ff in enumerate(yy):
			diff = abs(float(ff) - float(f))
			if diff < float(f)*threshold:
				score += 1
				yy.pop(k)
	return score

def octave_compare(y_pred, y, threshold):
	score = 0
	for f in y:
		for k, ff in enumerate(y_pred):
			diff = abs(float(ff) - float(f))
			diff2 = abs(float(ff*2) - float(f))
			diff3 = abs(float(ff*3) - float(f))
			diff4 = abs(float(ff/2) - float(f))
			diff5 = abs(float(ff/3) - float(f))
			if diff < float(f)*threshold:
				score += 1
				y_pred.pop(k)
			elif diff2 < float(f)*threshold:
			 	score += 1
			 	y_pred.pop(k)
			elif diff3 < float(f)*threshold:
			 	score += 1
			 	y_pred.pop(k)
			elif diff4 < float(f)*threshold:
			 	score += 1
			 	y_pred.pop(k)
			elif diff5 < float(f)*threshold:
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

def evaluate_kla(file_location, klapuri_location):
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
		try:
			prec += len(results_kla[k])
			rec += len(frame)
			score += compare(frame, results_kla[k], 0.03)

		except:
			pass
	print "Number of correct predicted:\t%i" % (score)	
	print "Number of predicted:\t\t%i" % (prec)
	print "Number of Ground Truth:\t\t%i" % (rec)
	print "Precision:\t\t\t%.4f" % (score/float(prec) if prec else 0)
	print "Recall:\t\t\t\t%.4f" % (score/float(rec) if rec else 0)	

	return score, prec, rec

def klapuri():
	filenames = fetchFiles('Maps', '.f0s')
	score = 0
	prec = 0
	rec = 0
	for path, fname in filenames:
		print "Evaluating " + fname
		GT_location = path + "/" + fname
		klapuri_location = 'Maps_noise_klapuri/' + fname
		s,p,r= evaluate_kla(GT_location, klapuri_location)
		score +=s
		prec +=p
		rec += r

	precision = (score/float(prec) if prec else 0)
	recall = (score/float(rec) if rec else 0)
	fscore = 2*recall*precision/(recall+precision)
	print "******************************************"
	print "Number of correct predicted:\t%i" % (score)	
	print "Number of predicted:\t\t%i" % (prec)
	print "Number of Ground Truth:\t\t%i" % (rec)
	print "Precision:\t\t\t%.4f" % precision
	print "Recall:\t\t\t\t%.4f" % recall
	print "F-score:\t\t\t%.4f" % fscore


def evaluate_ben(file_location, benetos_location):
	with open(file_location) as f:
		reader = np.loadtxt(f, delimiter = "\t")
	results_GT = []
	for line in reader:
		results_GT.append(filter (lambda a: a!= 0.0, line[1:]))

	with open(benetos_location) as f:
		reader_ben = csv.reader(f, delimiter = "\t")
		d = list(reader_ben)

	results_ben = []
	for line in d:
		b = np.array(filter (lambda a: a!= 0.0, line[1:]))
		results_ben.append(filter (lambda a: a!= '', b))


	score = 0
	prec = 0
	rec = 0
	i = 0
	for k, frame in enumerate(results_GT):
		if k%2:
			prec += len(results_ben[i])
			rec += len(frame)
			#score += octave_compare(frame, results_ben[k], 0.03)
			score += octave_compare(frame, results_ben[i], 0.03)
			i += 1


	return score, prec, rec

def benetos():
	filenames = fetchFiles('Maps', '.f0s')
	score = 0
	prec = 0
	rec = 0
	print len(filenames)
	for path, fname in filenames:
		#print "Evaluating " + fname
		GT_location = path + "/" + fname
		benetos_location = 'Maps_benetos/th_0.001/' + fname
		s,p,r = evaluate_ben(GT_location, benetos_location)
		score +=s
		prec +=p
		rec += r


	precision = (score/float(prec) if prec else 0)
	recall = (score/float(rec) if rec else 0)
	fscore = 2*recall*precision/(recall+precision)
	print "******************************************"
	print "Number of correct predicted:\t%i" % (score)	
	print "Number of predicted:\t\t%i" % (prec)
	print "Number of Ground Truth:\t\t%i" % (rec)
	print "Precision:\t\t\t%.4f" % precision
	print "Recall:\t\t\t\t%.4f" % recall
	print "F-score:\t\t\t%.4f" % fscore


def main():
	klapuri()
	#benetos()

if __name__ == "__main__":
    main()

