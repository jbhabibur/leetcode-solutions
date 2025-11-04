// Problem          :   LeetCode 485
// Problem Link     :   https://leetcode.com/problems/max-consecutive-ones/description/
// Intuition        :
//      1. Iterate through the array and count every consecutive 1 until you find a 0.
//      2. When you find a 0, update the max count variable if needed, 
//         and reset the count variable to start counting the next streak of consecutive 1's.
// Time Complexity  :   O(N)
// Space Complexity :   O(1)
// Language by      :   TypeScript

function findMaxConsecutiveOnes(nums: number[]): number {
    let count = 0, max = 0;

    for (let i = 0; i < nums.length; i++) {
        if (nums[i] == 1) {
            count++;
        } else {
            if (max < count) {
                max = count
            }
            count = 0
        }
    }

    if (max < count) {
        max = count
    }

    return max;
}

// Example usage
const nums = [1, 1, 0, 1, 1, 1]
console.log(findMaxConsecutiveOnes(nums));