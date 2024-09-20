class Solution(object):
    def contains_duplicate(self, nums):
        unique_nums = set()
        for num in nums:
            if num not in unique_nums:
                unique_nums.add(num)
            else:
                return True
        return False

solution = Solution()

def test_contains_duplicates():

	assert solution.contains_duplicate([1,2,3,1]) == True
	assert solution.contains_duplicate([]) == False
	assert solution.contains_duplicate([1,2,3,4]) == False
	assert solution.contains_duplicate([1,1,1,3,3,4,3,2,4,2]) == True
	assert solution.contains_duplicate([2]) == False
	assert solution.contains_duplicate([2, 2]) == True
	print("all tests passed")

test_contains_duplicates()
	