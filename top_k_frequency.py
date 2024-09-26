class Solution(object):
    def top_k_frequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        frequency_map = {}

        for num in nums:
            if num in frequency_map:
                frequency_map[num] += 1
            else:
                frequency_map[num] = 1
        
        bucket = [[] for _ in range(len(nums) + 1)]

        for num, freq in frequency_map.items():
            bucket[freq].append(num)
        
        return_list = []
        
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                return_list.append(num)
            if len(return_list) == k:
                return return_list


solution = Solution()

nums = [1,1,1,2,2,3]
# nums = []
k = 2

print(solution.top_k_frequency(nums, k))