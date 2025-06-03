from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = [] # List to store substrings that are found in other words

        # Iterate through each word in the list
        for i in range(len(words)):

            # Comparing with every other word
            for j in range(len(words)):
                # Make sure not comparing the same word with itself
                if i != j and words[i] in words[j]:
                    result.append(words[i])
                    break # No need to check other words once a match is found
        return result

# Example usage
solution = Solution()

words = ["leetcode","et","code"]
print(solution.stringMatching(words))

