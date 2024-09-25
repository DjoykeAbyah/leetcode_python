class Solution(object):
	def word_pattern(self, pattern, s):
		"""
		:type pattern: str
        :type s: str
        :rtype: bool
        """
		characters = list(pattern)
		words = s.split()

		if len(words) != len(characters):
			return False
		
		character_map = {}
		word_map = {}

		for word, character in zip(words, characters):
			if word in word_map:
				if word_map[word] != character:
					return False
			elif character in character_map:
				if character_map[character] != word:
					return False
			else:
				character_map[character] = word
				word_map[word] = character
		return True

solution = Solution()

pattern = "abba"
string = "cat dog dog cat"
# string = "cat dog dog fish"
# string = ""

print(solution.word_pattern(pattern, string))
				
