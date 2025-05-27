from typing import List

class TrieNode:
    def __init__(self):
        self.children = {} # Dictionary to store characters as child nodes
        self.is_end = False # Flag to mark the end of the word

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def _insert(self, digits):
        """Helper function to insert a single number as string in the Trie """

        current = self.root
        for char in digits:
            if char not in current.children: # If char is not already existed, add a new TrieNode
                current.children[char] = TrieNode()
            current = current.children[char] # Move to the next node
        current.is_end = True # Mark the end of number as string

    def build_trie(self, number):
        """Build the Trie with the given number"""

        self._insert(number)

    def find_length_of_prefix(self, prefix):
        """Return the length of the longest common prefix"""

        current = self.root
        count = 0
        for char in prefix:
            if char not in current.children: # If the current char is not existed, return the length of the currently common prefix
                return count
            count += 1
            current = current.children[char]
        return count # Return the final length of the common prefix

    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        for number in arr1:
            self.build_trie(str(number)) # Build the Trie with the given list of numbers

        max_length = 0
        for number in arr2:
            max_length = max(max_length, self.find_length_of_prefix(str(number)))  # Update the max length

        return max_length


# Example usage
solution = Solution()

arr1 = [1,10,100]
arr2 = [1000]

print(solution.longestCommonPrefix(arr1, arr2))
