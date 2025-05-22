class TrieNode:
    def __init__(self):
        self.children = {} # Dictionary to hold child nodes
        self.is_end_of_word = False # Indicates the end of a valid word in the Trie

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root

        for char in word:
            if char not in current.children: # Checking whether the character already exists
                current.children[char] = TrieNode() # Create a new node if it doesn't exist
            current = current.children[char] # Traverse to the next child node
        current.is_end_of_word = True # Indicates the end of a valid word

    def search(self, word):
        current = self.root

        for char in word:
            if char not in current.children: # Checking whether the character already exists
                return False # If it doesn't, the word isn't in the Trie
            current = current.children[char] # Traverse to the next node

        return current.is_end_of_word # Only return True if it's a complete word

    def startsWith(self, word: str) -> bool:
        current = self.root

        for char in word:
            if char not in current.children: # Checking whether the character already exists
                return False # If it doesn't, the word isn't in the Trie
            current = current.children[char] # Traverse to the next node

        return True # Return True if all characters in the prefix exist

    # Debugging purpose
    def display(self):
        result = [] # List to collect all complete words in the Trie

        def dfs(current, path, result):
            # If the current node marks the end of a word, add the word (path) to the result list
            if current.is_end_of_word:
                result.append(path)

            # Recursively visit all child nodes
            for char, next_node in current.children.items():
                dfs(next_node, path + char, result) # Append the character to the path and continue DFS

        # Start DFS traversal from the root node with an empty path
        dfs(self.root, "", result)

        print(result)

# Example usage
trie = Trie()

trie.insert("apple")
print(trie.search("apple")) # True
print(trie.search("app")) # False
print(trie.startsWith("app")) # True
trie.insert("app")
print(trie.search("app")) # True

trie.display()