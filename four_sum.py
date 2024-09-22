class Solution(object):
    def four_sum(self, nums, target):
        result_set = set()
        pair_map = {}
        nums_len = len(nums)

        for i in range(nums_len - 1):
            for j in range(i + 1, nums_len):
                pair_sum = nums[i] + nums[j]
                if pair_sum not in pair_map:
                    pair_map[pair_sum] = []
                pair_map[pair_sum].append((i, j))

        for i in range(nums_len - 1):
            for j in range(i + 1, nums_len):
                current_sum = nums[i] + nums[j]
                leftover_sum = target - current_sum

                if leftover_sum in pair_map:
                    for pair in pair_map[leftover_sum]: # check every pair containing that sum
                        x, y = pair
                        if i != x and i != y and j != x and i != y:
                            quadruplet = sorted([nums[i], nums[j], nums[x], nums[y]])
                            result_set.add(tuple(quadruplet)) # use add 
        result = []
        for quadruplet in result_set:
            result.append(list(quadruplet))
        return result

solution = Solution()

print(solution.four_sum([1, 0, -1, 0, -2, 2], 0))
# expected = [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

