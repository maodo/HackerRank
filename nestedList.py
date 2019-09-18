

if __name__ == '__main__':
	students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
	array_of_grades = []
	for student in students :
		print(student)
		array_of_grades.append(student[1])
	print(array_of_grades)
	min_arr = min([i for i in array_of_grades if i!=min(array_of_grades)])
	print(min_arr)