# Given an array of integers, return the sum of unique elements in the array.

def calculate_uniqueSum(array):
	
	if array:
		unique_values = set(array)
		total_value = 0
	else:
		print("array is empty")
		return 

	for value in unique_values:
		total_value += value
	return total_value

my_array = [1, 10, 8, 3, 2, 5, 7, 2, -2, -1]
# test with empty array
# my_array = []

return_sum = calculate_uniqueSum(my_array)
print(return_sum)