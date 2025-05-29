from typing import List

class TrieNode:
    def __init__(self):
        self.children = {} # Dictionary to characters as child nodes
        self.is_end = False # Flag to indicate the end of a complete word
        self.prefix_count = 0 # Counter to track how many words pass through this node

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def _insert(self, word):
        """Helper function to insert a single word into the Trie"""

        current = self.root
        for char in word:
            if char not in current.children: # If char is not already existed, add a new node
                current.children[char] = TrieNode()
            current = current.children[char] # Traverse to the next word
            current.prefix_count += 1 # Increment the counter by 1
        current.is_end = True # Mark the end of the word

    def _build_trie(self, words):
        """Helper function to build the Trie"""

        for word in words:
            self._insert(word)

    def sumPrefixScores(self, words: List[str]) -> List[int]:
        """Calculate the sum of prefix counts for each word"""

        self._build_trie(words)

        answer  = []
        for word in words:
            score = 0
            current = self.root
            for char in word:
                if char in current.children:
                    current = current.children[char]
                    score += current.prefix_count
            answer.append(score)

        return answer

# Example usage
solution = Solution()

words = ["abc", "ab", "bc", "b"]
print(solution.sumPrefixScores(words))