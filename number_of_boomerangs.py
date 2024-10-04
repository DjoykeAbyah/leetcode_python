class Solution(object):
    def number_of_boomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        total_boomerangs = 0

        for i in points:
            distance_count = {}
            for j in points:
                if j == i:
                    continue
                distance_x = j[0] - i[0]
                distance_y = j[1] - i[1]
                distance = distance_x * distance_x + distance_y * distance_y
                if distance not in distance_count:
                    distance_count[distance] = 0
                distance_count[distance] += 1
            
            for count in distance_count.values():
                if count > 1:
                    total_boomerangs += count * (count - 1)
            
        return total_boomerangs


solution = Solution()

points1 = [[0,0],[1,0],[2,0]]
points2 = [[1,1],[2,2],[3,3]]
points3 = [[1,1]]
points4 = [[]]

assert solution.number_of_boomerangs(points1) == 2
assert solution.number_of_boomerangs(points2) == 2
assert solution.number_of_boomerangs(points3) == 0
assert solution.number_of_boomerangs(points4) == 0
