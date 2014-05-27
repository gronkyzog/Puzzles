



# for k in range(1,10):
# 	print k
# 	for x in xrange(10**k,10**(k+1)):
# 		q,r = divmod(x,10)
# 		y = q + r*10**k 
# 		q,r = divmod(y,x)
# 		if r ==0 and x != y:
# 			print '%d,%d,%d' % (x,y,q)


#205128,820512,4
total = 0
for mult in range(1,10):
	for first_digit in range(1,10):
		digit = first_digit
		carry = 0
		sol = 0
		for k in range(100):
			carry,digit = divmod(digit*mult+carry,10)
			sol += digit*10**k
			if digit == first_digit and carry == 0 and sol > 10:
				shift_sol = str(sol/mult)
				shift_sol = int(shift_sol[-1]+shift_sol[:-1])
				if sol == shift_sol:
					total += sol/mult
					total = total % 10**5

print total
