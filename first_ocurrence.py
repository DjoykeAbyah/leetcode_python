# Given a string, return a string that contains only the first occurrence of each character in the string.

def find_first_occurence(array):
	if array:
		# Set removes duplicates, but it doesn't preserve the original order of elements
		seen = set()
		first_occurence_string = ""
	else:
		return

	for char in array:
		if char not in seen:
			first_occurence_string += char
			seen.add(char)
	return first_occurence_string

# my_string = "abracadabra"
# my_string = "Career Prep"
# my_string = "zzyzx"
my_string = ""

first_occurence_string = find_first_occurence(my_string)
print(first_occurence_string)
