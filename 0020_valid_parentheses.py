# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
#
#
# Example 1:
#
# Input: s = "()"
#
# Output: true
#
# Example 2:
#
# Input: s = "()[]{}"
#
# Output: true
#
# Example 3:
#
# Input: s = "(]"
#
# Output: false
#
# Example 4:
#
# Input: s = "([])"
#
# Output: true
#
# Example 5:
#
# Input: s = "([)]"
#
# Output: false
#
#
#
# Constraints:
#
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.


class Stack:
	def __init__(self) -> None:
		self._items = []

	def is_empty(self) -> bool:
		return not bool(self._items)

	def push(self, item: str) -> None:
		self._items.append(item)

	def pop(self) -> str:
		return self._items.pop()

	def peek(self) -> str:
		return self._items[-1]

	def size(self) -> int:
		return len(self._items)


class Solution:
	def isValid(self, s: str) -> bool:
		stack = Stack()
		mapping = {')': '(', ']': '[', '}': '{'}

		for i in s:
			if i not in mapping:
				stack.push(i)
			else:
				if stack.is_empty() or stack.peek() != mapping[i]:
					return False
				stack.pop()

		return stack.is_empty()
