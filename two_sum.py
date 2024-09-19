class Solution(object):
    def two_sum(self, nums, target):
        if len(nums) < 2:
           return []
        # create map with num as key and index as value
        num_map = {}
        # Loop through the list, storing the number and its index
        for i, num in enumerate(nums): # Loop through with both index and value
            # Find the number we need to add                       
            leftover = target - num
            # check if that number is in the map
            if leftover in num_map:
                # return index of that number an current index
                return [num_map[leftover], i] # Here we use i
            # Store the current number and its index in the map
            num_map[num] = i # Store the number with its index
        return []

solution = Solution()

def test_two_sum():
    # test 1
    assert solution.two_sum([2, 7, 11, 15], 9) == [0, 1]
    # test 2
    assert solution.two_sum([], 9) == []
    # test 3
    assert solution.two_sum([3, 2, 4], 6) == [1, 2]
    # test 4
    assert solution.two_sum([3, 3], 6) == [0, 1]
	# test 5
    assert solution.two_sum([0, 0], 6) == []
    print("all tests passed")

test_two_sum()