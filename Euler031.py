coins = [1,2,5,10,20,50,100,200]

def solve(target,subtotal,coin_list):
	output = []
	new_coinlist = list(coin_list)
	selected_coin = new_coinlist.pop()
	residual = target - subtotal
	max_size, r  = divmod(residual,selected_coin)
	if len(coin_list)==1: 
		if r != 0:
			return []
		return  [[(selected_coin,max_size)]]	
	max_size, r  = divmod(residual,selected_coin) 
	for i in range(0,max_size+1):
		sol = [(selected_coin,i)]
		sol_sum = selected_coin*i
		results = solve(target,sol_sum+subtotal,new_coinlist)
		for x in results:
			new_sol = list(sol)
			new_sol.extend(x)
			output.append(new_sol)
	return output

A = solve(200,0,coins)
print len(A)


