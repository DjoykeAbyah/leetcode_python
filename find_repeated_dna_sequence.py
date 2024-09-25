class Solution(object):
    def find_repeated_dna_sequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        sequence_map = {}
        return_list = []
        
        for i in range(len(s) - 9):
            substring = s[i:i+10]
            if substring in sequence_map:
                sequence_map[substring] += 1
            else:
                sequence_map[substring] = 1
        
        for sequence in sequence_map:
            if sequence_map[sequence] > 1:
                return_list.append(sequence)
        return return_list

solution = Solution()

string = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# string = "AAAAAAAAAAAAAAAAA"
# string = ""
# string = "AAA"


print(solution.find_repeated_dna_sequences(string))