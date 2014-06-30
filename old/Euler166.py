import itertools 

counter = 0
for i,(x1,x2,x3,x4) in enumerate(itertools.product(range(10),repeat=4)):
	s = x1+x2+x3+x4
	#max_x8 = max(min(s-x4,9),0)
	for x8 in xrange(10):
		for x12 in xrange(10):
			x16 = s - x4-x8-x12
			if x16 < 0 or x16>9:
				continue
			for x6 in xrange(10):
				x11 = s-x1-x6-x16
				if x11 < 0 or x11>9:
					continue

				for x5 in xrange(10):
					x7 =s- x5-x6-x8
					if x7 <0 or x7>9:
						continue
					x15 = s -x3-x7-x11
					if x15 < 0 or x15>9:
						continue

					for x9 in xrange(10):
						x13 = s-x1-x5-x9
						x10 = s-x9-x11-x12
						x14 = s-x13-x15-x16
						if x13 < 0 or x13>9:
							continue	
						if x10 < 0 or x10>9:
							continue	
						if x14 < 0 or x14>9:
							continue	

						if x4+x7+x10+x13==s and x5+x6+x7+x8==s and x2+x6+x10+x14==s:
							counter +=1

							if x1+x2+x3+x4 != s:
								raise

							if x5+x6+x7+x8 != s:
								raise
							
							if x9+x10+x11+x12 != s:
								raise

							if x13+x14+x15+x16 != s: 
								raise

							if x1+x5+x9+x13 != s: 
								raise

							if x2+x6+x10+x14 != s: 
								raise

							if x3+x7+x11+x15 != s: 
								raise

							if x4+x8+x12+x16 != s:
								raise

							if x1+x6+x11+x16 != s:
								raise

							if x4+x7+x10+x13 != s:
								raise



	print '%d,%d' %(i,counter)
print counter 
