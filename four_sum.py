class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()  # Sort the array to apply two-pointer technique
        result = []
        length = len(nums)

        for i in range(length - 3):
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicate first elements
                continue
            for j in range(i + 1, length - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:  # Skip duplicate second elements
                    continue
                
                left = j + 1
                right = length - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])  # Append the quadruplet
                        # Move pointers and skip duplicates for left
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        # Move pointers and skip duplicates for right
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        
        return result
            


