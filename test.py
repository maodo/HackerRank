import numpy
if __name__ == '__main__':
	a = "1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9"
	my_array = a.split(" ")
	my_array = numpy.array(my_array)
	my_array = my_array.astype(numpy.float)
	print(numpy.floor(my_array))
	print(numpy.ceil(my_array))
	print(numpy.rint(my_array))