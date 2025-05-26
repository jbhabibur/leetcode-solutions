from typing import List

class TrieNode:
    def __init__(self):
        self.children = {} # Dictionary to store characters as child nodes
        self.is_end = False # Flag to mark the end of a word

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def _insert(self, word):
        """Helper function to insert a single word in the Trie"""

        current = self.root
        for char in word:
            if char not in current.children: # If the char doesn't already exist, add a new TrieNode
                current.children[char] = TrieNode()
            current = current.children[char] # Move to the next node
        current.is_end = True # Mark the end of the word

    def build_trie(self, pattern):
        """Build the Trie with the given pattern"""

        self._insert(pattern)

    def _pattern_matching(self, query):
        """Return True if query matches with pattern else False"""

        current = self.root
        for char in query:
            if char in current.children:  # If char exits, pattern matches, move to the next character
                current = current.children[char]
            elif char not in current.children and char.isupper():  # If char doesn't exit and uppercase, pattern doesn't match, return false
                return False

            # If char doesn't exit and lowercase, pattern matches, skip the current iteration

        return current.is_end # True: Query matches with pattern, indicate pattern is a valid and complete word in the Trie

    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        self.build_trie(pattern) # Build the Trie with the given pattern

        result = []
        for query in queries:
            result.append(self._pattern_matching(query)) # Return True if query matches with pattern else False

        return result


# Example usage
solution = Solution()

queries = ["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"]
pattern = "FoBaT"

print(solution.camelMatch(queries, pattern))
