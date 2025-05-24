from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def _insert(self, word):
        """Helper function to insert each word in the Trie"""

        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end = True

    def build_trie(self, number):
        self._insert(str(number)) # Convert each number into string

    def display(self):
        def _dfs(current, path, result):
            if current.is_end:
                result.append(int(path))

            for char, next_node in current.children.items():
                _dfs(next_node, path + char, result)

        result = []
        _dfs(self.root, "", result)

        return result

    def lexicalOrder(self, n: int) -> List[int]:
        # Build trie by inserting each number from 1 to n
        for number in range(1, n + 1):
            self.build_trie(number)

        result = self.display()

        return result


# Example usage
solution = Solution()

n = 13
print(solution.lexicalOrder(n))





