

if __name__ == '__main__':
	students = []
	for _ in range(int(input())):
		name = input()
		score = float(input())
		students.append([name,score])
	# print(students)
	# students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
	array_of_grades = []
	for student in students :
		array_of_grades.append(student[1])
	# print(min(array_of_grades))
	min_arr = min([i for i in array_of_grades if i!=min(array_of_grades)])
	# print(min_arr)
	lowest_grades = [students[i][0] for i in range(len(students)) if students[i][1]==min_arr]
	lowest_grades.sort()
	for lowest_grade in lowest_grades :
		print(lowest_grade)
			