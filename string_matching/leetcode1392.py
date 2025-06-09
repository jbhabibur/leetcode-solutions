def lps(pattern):
    """Compute the Longest Prefix Suffix (LPS) array for the given pattern"""

    m = len(pattern)
    lps_arr = [0] * m  # Initialize LPS array with 0

    i = 1           # Initialize pointer to traverse the pattern from the second character
    length = 0      # Length of the previous longest prefix suffix

    while i < m:
        if pattern[i] == pattern[length]:
            # When characters match, increment length and assign it to lps_arr[i]
            length += 1
            lps_arr[i] = length
            i += 1
        else:
            if length != 0:
                # Fall back in the lps_arr if there is a mismatch after some matches
                length = lps_arr[length - 1]
            else:
                # No match found; move to the next character
                lps_arr[i] = 0
                i += 1

    return lps_arr  # Final LPS array

class Solution:
    def longestPrefix(self, s: str) -> str:
        # Compute LPS array of the string
        lps_arr = lps(s)
        print(lps_arr)  # Debug: print LPS array

        if lps_arr[-1] != 0:
            return s[:lps_arr[-1]]
        else:
            return ""

# Example usage
sol = Solution()
s = "ababab"
print(sol.longestPrefix(s))
