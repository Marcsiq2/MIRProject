"""
degradation_test.py

validate that the audio-degradation-toolbox can be usedd in python

2016-07-16 Feng Liu fengliu@uvic.ca
"""
import matlab.engine
eng = matlab.engine.start_matlab()

'''
this is used to add search path for matlab, as the .m files are 
saved in this folder.
'''
eng.addpath('../audio-degradation-toolbox')
eng.demo_degradations(nargout = 0)