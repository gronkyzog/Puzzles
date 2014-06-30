def test():
	strMap = {
	1: 'one',
	2: 'two',
	3: 'three',
	4: 'four',
	5: 'five',
	6: 'six',
	7: 'seven',
	8: 'eight',
	9: 'nine',
	10: 'ten',
	11: 'eleven',
	12: 'twelve',
	13: 'thirteen',
	14: 'fourteen',
	15: 'fifteen',
	16: 'sixteen',
	17: 'seventeen',
	18: 'eighteen',
	19: 'nineteen',
	20: 'twenty',
	30: 'thirty',
	40: 'forty',
	50: 'fifty',
	60: 'sixty',
	70: 'seventy',
	80: 'eighty',
	90: 'ninety',
	100: 'one hundred',
	200: 'two hundred',
	300: 'three hundred',
	400: 'four hundred',
	500: 'five hundred',
	600: 'six hundred',
	700: 'seven hundred',
	800: 'eight hundred',
	900: 'nine hundred',
	1000: 'one thousand'
	}


	def onehundred(x):
		if x <=20:
			s = strMap[x]
		elif x > 20:
			tens = 10*(x/10)
			ones = x % 10
			if ones != 0:
				s = strMap[tens] + ' ' + strMap[ones]
			else:
				s = strMap[tens]
		return s 

	output = []
	for i in range(1,1001):
		try:
			hundreds = 100*(i/100)
			decimal = i % 100
			if hundreds == 0:
				output.append(onehundred(i))
			else:
				if decimal == 0:
					output.append(strMap[hundreds])
				else:
					output.append(strMap[hundreds] + ' and ' + onehundred(decimal))
		except Exception,ex:
			print 'Error %d,%d, %d' %(i,hundreds,decimal)
			print ex
			raise

	count = 0
	for x in output:
		count = count + len(x.replace(' ',''))
		#print '%s,%d' %(x,count)
	return count

if __name__ == '__main__':
    print test()