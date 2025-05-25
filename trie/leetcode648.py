from typing import List

class TrieNode:
    def __init__(self):
        self.children = {} # Dictionary to store characters as child nodes
        self._is_end = False # Flag to mark the end of a word

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def _insert(self, word):
        """Helper function to insert a single word in the Trie"""

        current = self.root
        for char in word:
            if char not in current.children: # If char is not already present, add a new node
                current.children[char] = TrieNode()
            current = current.children[char] # Move to the next node
        current._is_end = True # Mark the end of the word

    def build_trie(self, words):
        """Build the Trie from the given words of the dictionary"""

        for word in words:
            self._insert(word)

    def _contains(self, word):
        """Check if a word is derivative of a root?"""

        current = self.root
        path = ""
        for char in word:
            if current._is_end: # If True, word is a derivative of a root
                return True, path
            if char not in current.children: # If char is not already present, word is not a derivative of a root
                return False, ""
            path = path + char # Concatenating the root word
            current = current.children[char] # Move to the next node

        return current._is_end, path if current._is_end else ""

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        """Return the sentence after the replacement of the derivative words with its root words"""

        self.build_trie(dictionary) # Build the Trie from the given dictionary

        result = []
        for word in sentence.split(): # Split the sentence into words
            # Check if the word is derivative? Return tuple that consist (, root)
            (is_prefix, replace_word) = self._contains(word)
            if is_prefix: # If word is a derivative, replace with the root
                result.append(replace_word)
            else: # Otherwise, keep the original word
                result.append(word)

        return " ".join(result)

# Example usage
solution = Solution()

dictionary = ["a","b","c"]
sentence = "aadsfasf absbs bbab cadsfafs"
print(solution.replaceWords(dictionary, sentence))