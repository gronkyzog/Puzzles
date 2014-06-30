import sys
sys.path.append('./problems/')
import os
import eulertools
import subprocess
import glob
import datetime


files = glob.glob('./problems/Euler*.py')


questions = range(1,40)
for q in questions:
	try:
		question = 'Euler'+ (3-len(str(q)))*'0' + str(q)
		problem = __import__(question)
		start = datetime.datetime.now()
		solution = problem.test()
		end = datetime.datetime.now()
		print '%s,%s,%s,%d' %(question,solution,eulertools.answerhash[q]==hash(str(solution)),(end-start).microseconds/1000)
	except:
		print 'Failed' , q
		#raise

