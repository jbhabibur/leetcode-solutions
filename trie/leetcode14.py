from typing import List

class TrieNode:
    def __init__(self):
        self.children = {} # Dictionary to hold child nodes
        self._is_end_of_word = False # Indicates the end of a word

class Solution:
    def __init__(self):
        self.root = TrieNode() # Initialize, the root of the Trie

    def build(self, words: List[str]):
        # Helper function to insert a word into the Trie
        def _insert(word: str):
            current = self.root
            for char in word:
                # If the character is not already a child, add it
                if char not in current.children:
                    current.children[char] = TrieNode()
                # Move to the child node
                current = current.children[char]
            # Mark the end of the word
            current._is_end_of_word = True

        for word in words:
            _insert(word)

    def longestCommonPrefix(self, strs: List[str]) -> str:
        self.build(strs) # Build Trie from the list of words

        prefix = "" # To accumulate the longest common prefix

        # DFS to find the longest common prefix
        def _dfs(current, path):
            # Stop if the current node has more than one child (branch)
            # Or, if it is the end of a word (word boundary)
            if len(current.children) != 1 or current._is_end_of_word:
                return path

            # Continue DFS on the only child node
            for char, next_node in current.children.items():
                return _dfs(current.children[char], path + char)

        # Start DFS from the root node
        return _dfs(self.root, prefix)

# Example usage
solution = Solution()

strs = ["flower","flow","flight"]
print(solution.longestCommonPrefix(strs)) # "fl"

