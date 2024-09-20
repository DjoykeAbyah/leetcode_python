class Solution(object):
    def single_number(self, nums):
        if not nums:
           return 
        unique_set = set()
        for num in nums:
            if num not in unique_set:
                unique_set.add(num)
            else:
                unique_set.remove(num)
        return unique_set.pop()

solution = Solution()

def test_single_number():
	assert solution.single_number([4,1,2,1,2]) == 4
	assert solution.single_number([]) == None
	assert solution.single_number([2,2,1]) == 1
	assert solution.single_number([5]) == 5

test_single_number()