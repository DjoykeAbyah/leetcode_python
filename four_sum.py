class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        pair_map = {}
        result_set = []
        nums_len = len(nums)

        for i in range(nums_len - 1):
            for j in range(nums_len + 1, nums_len):
                pair_sum = nums[i] + nums[j]
                if pair_sum not in pair_map:
                   pair_map[pair_sum] = []  # Creating an empty list if pair_sum key is not in the dictionary
                pair_map[pair_sum].append(i, j) # appending the indexes as a tuple making it immutable

        for i in range(nums_len - 1):
            for j in range(nums_len + 1, nums_len):
                current_sum = nums[i] + nums[j]
                remain_sum = target - current_sum

            if remain_sum in pair_map:
                for pair in pair_map[remain_sum]:
                    x, y = pair # tuple unpacking
                    quadruplet = sorted[nums[i], nums[j], nums[x], nums[y]] # sorted to avoid duplicates
                    result_set.add(tuple(quadruplet)) # Add as a tuple to avoid duplicates If you tried to add a list directly to a set, you would encounter a TypeError.
        return list(quadruplet)	

		
			



        