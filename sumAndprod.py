import numpy as np
if __name__ == '__main__':	
	a = []
	my_array = []
	# map function which allows us to get string input and convert it to int
	N,M = map(int, input().split())
	
	for i in range(N):
		a.append(input())
	'''
		
	'''
	for elt in a:
		my_array.append(elt.split(" "))
	my_array = np.array(my_array)
	my_array = my_array.astype(np.int)
	print(my_array)
	print( np.prod(np.sum(my_array, axis = 0)))
