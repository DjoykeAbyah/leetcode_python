from collections import Counter

def has_zero_sum_2(array):
    count = Counter(array)
    pairs = []

    for num in count:
        if num == 0:
            # Handle zeroes: pairs of (0, 0)
            pair_count = count[num] // 2
            pairs.extend([(0, 0)] * pair_count)
        elif num > 0 and -num in count:
            # For non-zero pairs: find pairs of (num, -num)
            pair_count = max(count[num], count[-num])
            pairs.extend([(num, -num)] * pair_count)

    return pairs

# Test cases
my_array = [1, 10, 8, 3, 2, 5, 7, 2, -2, -1]
empty_array = []
no_pair_array = [1, 2]
same_value_array = [1, 1]
one_pair_array = [1, -1]
negative_pair_array = [-1, -1]

result = has_zero_sum_2(my_array)
print(result)

result = has_zero_sum_2(empty_array)
print(result)

result = has_zero_sum_2(no_pair_array)
print(result)

result = has_zero_sum_2(same_value_array)
print(result)

result = has_zero_sum_2(one_pair_array)
print(result)

result = has_zero_sum_2(negative_pair_array)
print(result)
