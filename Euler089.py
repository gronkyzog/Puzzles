import csv 

def extract_digits(x):
	output = []
	r = x 
	while r >0:
		r,k = divmod(r,10)
		output.append(k) 
	return output


csvreader = csv.reader(open('euler089.txt','r'))

A = [x[0] for x in csvreader]

romanMap = {}
romanMap['I'] = 1
romanMap['V'] = 5
romanMap['X'] = 10
romanMap['L'] = 50
romanMap['C'] = 100
romanMap['D'] = 500
romanMap['M'] = 1000

RD = []
RD.append(["","I","II","III","IV","V","VI","VII","VIII","IX"])
RD.append(["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"])
RD.append(["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"])
RD.append(["","M","MM","MMM","MMMM"])


total = 0
total2 = 0
for a in A:
	f = [romanMap[s] for s in a]
	for i in range(len(f)-1):
		if f[i] < f[i+1]:
			f[i] *= -1
	y = sum(f)
	dy = extract_digits(y)
	roman = [RD[i][d] for i,d in enumerate(dy)]
	roman = roman[::-1]
	b = ''.join(roman)
	total += len(a) - len(b)
	print '%s,%s,%d,%d,%d' % (a,b,sum(f),total,total2)



