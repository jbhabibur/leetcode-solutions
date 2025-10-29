/*  
    LeetCode Problem    :   455. Assign Cookies  
    Link                :   https://leetcode.com/problems/assign-cookies/description/  
    Intuition           :
        a. Sort children by their “greed factor” (how big a cookie they need).  
        b. Sort cookies by size.  
        c. Use two pointers: one for children (`i`), one for cookies (`j`).  
        d. For each cookie in increasing size, if it meets the current child’s greed, assign it (and move to next child).  
        e. Continue until we run out of children or cookies.  
        f. The number of children we satisfy = `i`.  
*/

function findContentChildren(g: number[], s: number[]): number {
    // Sort both arrays to ensure we're matching the `easiest` children first
    g.sort((a, b) => a - b);
    s.sort((a, b) => a - b);

    const m = g.length;
    const n = s.length;

    let i = 0; // pointer for children
    let j = 0; // pointer for cookies

    // While there are children left and cookies left
    while (i < m && j < n) {
        if (s[j] >= g[i]) {
            // Cookie j can satisfy child i
            i++;
        }
        // Whether we assigned or not, move to next cookie
        j++;
    }

    // `i` is the count of children satisfied
    return i;
};

// Example usage
const g = [1, 2, 3];
const s = [1, 1];
console.log(findContentChildren(g, s));
