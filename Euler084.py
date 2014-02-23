import random
import numpy

Board = ['GO','A1','CC1','A2','T1','R1','B1','CH1','B2','B3','JAIL',
		 'C1','U1','C2','C3','R2','D1','CC2','D2','D3',
		 'FP','E1','CH2','E2','E3','R3','F1','F2','U2','F3','GTJ',
		 'G1','G2','CC3','G3','R4','CH3','H1','T2','H2']


Chance = ['GO','JAIL','C1','E3','H2','R1','+R','+R','+U','-3',None,None,None,None,None,None]
Community = ['GO','JAIL',None,None,None,None,None,None,None,None,None,None,None,None,None,None]

random.shuffle(Chance)
random.shuffle(Community)

print len(Board)
print len(Chance)
print len(Community)
nsquares = len(Board)
tally = [0 for i in range(nsquares)]
pos = 0
doublecount = 0
samples = 10**8
for i in range(0,samples):
	roll1 = random.randint(1,6)
	roll2 = random.randint(1,6)
	total = roll1+roll2
	if roll1 == roll2:
		doublecount +=1
	else:
		doublecount =0

	if doublecount ==3:
		pos = Board.index('JAIL')
		doublecount = 0
	else:
		pos = (pos +total) % nsquares

		if pos in (Board.index('CC1'),Board.index('CC2'),Board.index('CC3')):
			card = Community.pop(0)
			Community.append(card)
			if card in  ('GO','JAIL','C1','E3','H2','R1'):
				pos = Board.index(card)



		if pos in (Board.index('CH1'),Board.index('CH2'),Board.index('CH3')):
			card = Chance.pop(0)
			Chance.append(card)
			if card in  ('GO','JAIL','C1','E3','H2','R1'):
				pos = Board.index(card)
			elif card == '-3':
				pos = (pos -3) % nsquares
			elif card == '+R' and Board.index('CH1'): 
				pos = Board.index('R2')

			elif card == '+R' and Board.index('CH2'): 
				pos = Board.index('R3')

			elif card == '+R' and Board.index('CH3'):
				pos = Board.index('R1')


			elif card == '+U' and Board.index('CH1'):
				pos = Board.index('U1')

			elif card == '+U' and Board.index('CH2'):
				pos = Board.index('U2')

			elif card == '+U' and Board.index('CH3'):
				pos = Board.index('U1')


		if pos == Board.index('GTJ'):
			pos = Board.index('JAIL')

		


	tally[pos] +=1
	
I = numpy.argsort(tally)[::-1]

for i in I:
	print i,Board[i],(1.0*tally[i])/samples


print I[0]*10000 + I[1]*100 + I[2]