from typing import List

def starts_with_prefix(word, pref):
    """Return True if the given word starts with the prefix `pref`"""

    # A word cannot start with a prefix if it's shorter than the prefix
    if len(word) < len(pref):
        return False

    i = j = 0
    # Compare characters from the beginning of both the word and the prefix
    while j < len(pref):
        if word[i] != pref[j]: # If the corresponding characters mismatched
            return False

        i += 1
        j += 1

    return True # All corresponding characters matched

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0

        for word in words:
            # Check if the word starts with the given prefix using helper function
            if starts_with_prefix(word, pref):
                count += 1

        return count

# Example usage
solution = Solution()

words = ["leetcode","win","loops","success"]
pref = "code"
print(solution.prefixCount(words, pref))