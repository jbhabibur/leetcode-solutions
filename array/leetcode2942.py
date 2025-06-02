from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result = []

        for i in range(len(words)):
            for j in range(len(words[i])):
                if x == words[i][j]:
                    result.append(i)
                    break

        return result

# Example usage
solution = Solution()

words = ["leet","code"]
x = "e"
print(solution.findWordsContaining(words, x))
