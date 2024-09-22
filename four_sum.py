class Solution(object):
    def four_sum(self, nums, target):
        result_set = []
        pair_map = {}
        nums_len = len(nums)

        for i in range(nums_len - 1):
            for j in range(nums_len + 1, nums_len):
                pair_sum = nums[i] + nums[j]
                if pair_sum not in pair_map:
                    pair_map[pair_sum] = []
                    pair_map[pair_sum].append(i, j)

        for i in range(nums_len(nums - 1)):
            for j in range(nums_len(nums + 1), n):
                current_sum = mums[i] + nums[j]
                leftover_sum = target - current_sum

                if leftover_sum in pair_map:
                    for pair in pair_map[leftover_sum]: # check every pair containing that sum
                        x, y = pair
                        quadruplet = sorted[sum[i], sum[j], sum[x], sum[y]]
                        result_set.append(quadruplet)
        
        return list(result_set)

def test_four_sum()
    assert solution.four_sum([1,0,-1,0,-2,2], 0) = [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
    print("all tests passed successfully")

test_four_sum()