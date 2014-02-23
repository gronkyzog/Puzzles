import csv
cards = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
suits = ['S','C','D','H']

rank  = ['HC','1P','2P','3K','ST','FL','FH','4K','SF']




def high_card(X):
	A = [a[0] for a in X]	
	Y = [cards.index(a) for a in A]
	Y.sort(reverse = True)
	Z = [cards[y] for y in Y]
	return Z

def is_n_of_a_kind(X,n):
	A = [a[0] for a in X]
	B = []
	for c in cards:
		if A.count(c) == n:
			B.append(c)

	hand = [cards.index(a) for a in B]
	hand.sort(reverse = True)
	remainder = [x for x in X if x[0] not in B]
	hand = [cards[h] for h in hand]
	return hand,remainder

def is_flush(X):
	A = [a[1] for a in X]
	for x in suits:
		if A.count(x)==5:
			b = max([cards.index(a[0]) for a in X])
			return cards[b]
	return None
	 	
def is_straight(X):
	A = list(set([cards.index(a[0]) for a in X]))
	if len(A)<5: 
		return None
	A.sort()
	if A[4]-A[0]==4:
		return cards[A[4]]

	elif A[3]-A[0]==3 and A[4]==12 and A[0]==0:
		return cards[A[3]]

	else:
		return None

def is_straight_flush(X):
	ST =  is_straight(X)
	FL =  is_flush(X)
	if ST is not None and FL is not None:
		return ST



def rank_hand(X):
	SF = is_straight_flush(X)
	if SF is not None:
		return ('SF',SF)
	K4,R4 = is_n_of_a_kind(X,4)
	if len(K4) > 0:
		HC = high_card(R4)
		hand = ['4K',K4]
		hand.extend(HC)
		return hand

	FL = is_flush(X)
	if FL is not None:
		return ['FL',FL]

	ST = is_straight(X)
	if ST is not None:
		return ['ST',ST]

	K3,R3 = is_n_of_a_kind(X,3)
	K2,R2 = is_n_of_a_kind(X,2)
	if len(K3)>0 and len(K2)>0:
		return ['FH',K3[0],K2[0]]

	elif len(K3)>0 and len(K2)==0:
		output = ['3K',K3[0]]
		HC = high_card(R3)
		output.extend(HC)
		return output

	elif len(K3)==0 and len(K2)==2:
		output = ['2P',K2[0],K2[1]]
		HC = high_card(R2)
		output.extend(HC)
		return output

	elif len(K3)==0 and len(K2)==1:
		output = ['1P',K2[0]]
		HC = high_card(R2)
		output.extend(HC)
		return output
	else:
		output = ['HC']
		output.extend(high_card(X))
		return output

	
def winning_hand(X,Y):
	Hx = rank.index(X[0]) 
	Hy = rank.index(Y[0]) 
	if Hx > Hy:
		return 1
	elif Hx < Hy:
		return 2
	else:
		for x,y in zip(X[1:],Y[1:]):
			if cards.index(x) > cards.index(y):
				return 1
			elif cards.index(x) < cards.index(y):
				return 2 
		return 0





csvreader = csv.reader(open('Euler054.txt','rb'),delimiter=' ')
hands = []
counter = 0
for row in csvreader:
	L = row[:5]
	R = row[5:]
	LH = [(x[0],x[1]) for x in L]
	RH = [(x[0],x[1]) for x in R]
	LR= rank_hand(LH)
	RR = rank_hand(RH)
	z = winning_hand(LR,RR)
	if z ==1:
		counter +=1
		print L,R,LR,RR,z

	

print counter
	
