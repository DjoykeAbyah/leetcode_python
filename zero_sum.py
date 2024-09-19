def has_zero_sum(array):
	seen = set()
	pairs = []

	for num in array:
		if -num in seen:
			pairs.append((num, -num))
		seen.add(num)
	return pairs

#example array
my_array = [1, 10, 8, 3, 2, 5, 7, 2, -2, -1]

result = has_zero_sum(my_array)
print(result)
