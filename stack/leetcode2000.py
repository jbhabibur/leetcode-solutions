class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        stack = [] # Stack to store characters in LIFO order
        flag = -1 # Flag to mark the index where `ch` is found

        for i in range(len(word)):
            stack.append(word[i]) # Push character to stack
            if word[i] == ch:
                flag = i # Save the index where `ch` is found
                break  # Stop after finding first occurrence

        result = ""
        # If `ch` was found, reverse the prefix using the stack
        if flag != -1:
            for i in range(len(stack)):
                result += stack.pop() # Pop reverses the prefix

        # Append the rest of the word if any
        return result + word[flag + 1:]

# Example usage
sol = Solution()

word = "abcd"
ch = "z"
print(sol.reversePrefix(word, ch))