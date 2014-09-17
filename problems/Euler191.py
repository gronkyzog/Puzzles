# import itertools



# def generate_sequence_bf(n):
# 	counter = 0
# 	mapper = {}
# 	for x in itertools.product(['O','L','A'],repeat =n):
# 		y = ''.join(x)
# 		key = (y,min(y.count('L'),2),'AAA' in y)
# 		mapper[key]=1

# 	return mapper


# def next_cycle(oldmap):
# 	mapper = {}
# 	for x in ['O','A','L']:
# 		for k,v in oldmap.items():
# 			w = list(k)
# 			if x == 'L':
# 				w[1] = min(2,w[1]+1)
# 			if (x == 'A' and w[0]=='AA'): # or w[2]==True:
# 				w[2]= True

# 			w[0] = x + w[0][0]
# 			key = tuple(w)
# 			if key not in mapper:
# 				mapper[key]=0
# 			mapper[key] +=v

# 	return mapper

# def count_solutions(mapper):
# 	return sum([v for k,v in mapper.items() if k[1]<2 and k[2]== False])


# A = generate_sequence_bf(2)
# for i in range(3,31):
# 	A = next_cycle(A)
# 	print i,count_solutions(A)



f_db={};
def func(left,nl,na):
    if(nl>=3): return 0;
    if(na>1): return 0;
    if(left<=0): return 1;
    
    key=tuple([left,nl,na])
    if(key in f_db): return f_db[key];
    
    total=0;
    total+=func(left-1,0,na); # 'O'
    total+=func(left-1,nl+1,na); # 'L'
    total+=func(left-1,0,na+1);  # 'A'
    
    f_db[key]=total;
    return total;

#===================

total=func(30,0,0);
print "Total: %d"%total;
