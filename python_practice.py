def average(numbers):
	ave = 0
	count = 0
	for number in numbers:
		ave = ave + number
		count = count + 1

	return ave/count

print(average([1, 5, 9]))
print(average(range(11)))