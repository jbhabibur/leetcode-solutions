def search_with(word, prefix):
    """Return True if 'word' starts with the given 'prefix'"""

    # If word is shorter than prefix, it can't match
    if len(word) < len(prefix):
        return False

    for i in range(len(prefix)):
        # Compare characters of word and prefix one by one
        if word[i] != prefix[i]:
            return False

    # All characters matched
    return True

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        # Split sentence into individual words
        words = sentence.split()

        # Check each word to see if it starts with searchWord
        for i, word in enumerate(words):
            # Search each words with the given prefix
            match = search_with(word, searchWord)

            if match:
                return i + 1 # 1-based index

        # No word found starting with searchWord
        return -1

# Example usage
sol = Solution()

sentence = "i love eating burger"
searchWord = "burg"
print(sol.isPrefixOfWord(sentence, searchWord))
