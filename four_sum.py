class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """ 
        nums.sort()  # sort array
        result = []  # create list for result
        n_len = len(nums)

        for i in range(n_len - 3):  # leave space for 3 other nums
            if i > 0 and nums[i] == nums[i - 1]:  # if duplicate
                continue
            for j in range(i + 1, n_len - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
				
				# use two pointers for the remaining two numbers
                left = j + 1
                right = n_len - 1
                while left < right:
                    total = nums[i], nums[j], nums[left], nums[right]
                    if total == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
						# move pointers and skip duplicates
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        return result

