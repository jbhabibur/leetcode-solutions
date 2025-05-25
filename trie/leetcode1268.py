from typing import List

class TrieNode:
    def __init__(self):
        self.children = {} # Dictionary to store each character as a node
        self.is_end = False # Indicate the end of the word

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def _insert(self, word: str) -> None:
        """Helper function to insert a single word in the Trie"""

        current = self.root
        for char in word:
            if char not in current.children: # If the char is not already present, add a new node
                current.children[char] = TrieNode()
            current = current.children[char] # Traverse to the next node
        current.is_end = True # Mark the end of the node

    def build_trie(self, products):
        """Build the Trie from the list of products"""

        for product in products:
            self._insert(product)

    def _dfs(self, current, path, result):
        """Perform DFS to collect upto 3 lexicographical words"""

        if current.is_end:
            if len(result) == 3: # Upto 3 lexicographical words
                return
            result.append(path)

        for char, next_node in sorted(current.children.items()): # Traverse children in lexicographical order
            self._dfs(next_node, path + char, result)

    def starts_with(self, prefix):
        """Return upto 3 lexicographical words starting with the given prefix"""

        current = self.root
        for char in prefix:
            if char not in current.children: # If the char in the prefix is not present, return empty list
                return []
            current = current.children[char] # Traverse to the next children

        result = []
        self._dfs(current, prefix, result) # Start DFS from prefix

        return result

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        """Return a list of lists of the suggested products after each character of searchWord is typed"""

        self.build_trie(products) # Build the Trie from the products list

        answer = []
        for i in range(len(searchWord)):
            suggested_products = self.starts_with(searchWord[:i + 1]) # Get suggestions for the current prefix
            answer.append(suggested_products)

        return answer

# Example usage
solution = Solution()

products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"

print(solution.suggestedProducts(products, searchWord))

