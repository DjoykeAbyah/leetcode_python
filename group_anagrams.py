class Solution(object):
    def group_anagrams(self, strs):
        anagram_map = {}

        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            
            key = tuple(count)
            if key not in anagram_map:
                anagram_map[key] = []
            anagram_map[key].append(word)

        return list(anagram_map.values())

solution = Solution()

strings = ["eat","tea","tan","ate","nat","bat"]
# strings = []
print(solution.group_anagrams(strings))
