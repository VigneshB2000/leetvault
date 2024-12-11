# Given an array of string words, return all strings in words that is a substring of another word. You can return the answer in any order.
#
# A substring is a contiguous sequence of characters within a string
#
#
#
# Example 1:
#
# Input: words = ["mass","as","hero","superhero"]
# Output: ["as","hero"]
# Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
# ["hero","as"] is also a valid answer.
# Example 2:
#
# Input: words = ["leetcode","et","code"]
# Output: ["et","code"]
# Explanation: "et", "code" are substring of "leetcode".
# Example 3:
#
# Input: words = ["blue","green","bu"]
# Output: []
# Explanation: No string of words is substring of another string.
#
#
# Constraints:
#
# 1 <= words.length <= 100
# 1 <= words[i].length <= 30
# words[i] contains only lowercase English letters.
# All the strings of words are unique
#

class Solution:
	def stringMatching(self, words: List[str]) -> List[str]:
		result_list = []
		for element_1 in words:
			for element_2 in words:
				if element_1 == element_2:
					continue
				elif element_2.find(element_1) != -1 and element_1 not in result_list:
					result_list.append(element_1)
		return result_list

.