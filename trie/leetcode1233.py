from typing import List

class TrieNode:
    def __init__(self):
        self.children = {} # Dictionary to store characters as child nodes
        self.is_end = False # Indicate to end of a complete word

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def _insert(self, word):
        """Helper function to insert a single word in the Trie"""

        current = self.root
        for char in word:
            if char not in current.children: # If char is not already existed, add a new node
                current.children[char] = TrieNode()
            current = current.children[char] # Traverse to the next node
        current.is_end = True # Mark to end the word

    def build_trie(self, words):
        """Build Trie with the given list of folders"""

        for word in words:
            self._insert(word.split("/")) # ["a", "b", "ca"]

    def is_subfolder(self, prefix):
        """Return True if the given prefix represents a subfolder"""

        current = self.root
        flag = False
        for char in prefix.split("/"):
            if char not in current.children:
                return False
            if current.is_end: # True: A complete folder path ends here, so the prefix is a subfolder
                flag = True
            current = current.children[char]
        return flag

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        self.build_trie(folder)

        result = []
        for folder_path in folder:
            if self.is_subfolder(folder_path):
                continue
            else:
                result.append(folder_path)
        return result

# Example usage
solution = Solution()

folder = ["/a/b/c","/a/b/ca","/a/b/d"]
print(solution.removeSubfolders(folder))