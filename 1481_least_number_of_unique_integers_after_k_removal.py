# Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.
#
#
#
# Example 1:
#
# Input: arr = [5,5,4], k = 1
# Output: 1
# Explanation: Remove the single 4, only 5 is left.
# Example 2:
# Input: arr = [4,3,1,1,3,3,2], k = 3
# Output: 2
# Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.
#
#
# Constraints:
#
# 1 <= arr.length <= 10^5
# 1 <= arr[i] <= 10^9
# 0 <= k <= arr.length

class Solution:
	def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
		count_dict = {}
		for element in arr:
			if element in count_dict:
				count_dict[element] += 1
			else:
				count_dict[element] = 1

		count_freq = sorted(count_dict.values())
		unique_count = len(count_freq)
		for count in count_freq:
			if k >= count:
				k -= count
				unique_count -= 1
			else:
				break
		return unique_count





