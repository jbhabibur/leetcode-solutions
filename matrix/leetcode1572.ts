/*
    Problem             : Matrix Diagonal Sum
    Link                : https://leetcode.com/problems/matrix-diagonal-sum/description/
    Intuition           :
        a.  For each iteration, we adds both diagonals elements
        b.  Remove middle elment if counted twice (odd-sized matrix)
    Time complexity     : O(n)
    Space complexity    : O(1)
    Language by         : TypeScript
*/

function diagonalSum(mat: number[][]): number {
    const n = mat.length;
    let sum = 0;

    // Add primary + secondary diagonal elements
    for (let i = 0; i < n; i++) {
        sum += mat[i]![i]!;
        sum += mat[i]![n - i - 1]!;
    }

    // Remove middle element if counted twice (odd-sized matrix)
    if (n % 2 !== 0) {
        const mid = Math.floor(n / 2);
        sum -= mat[mid]![mid]!;
    }

    return sum;
}

// Example
const mat = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1]
];

console.log(diagonalSum(mat));