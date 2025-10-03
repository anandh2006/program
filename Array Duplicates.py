Given an array arr[] of size n, containing elements from the range 1 to n, and each element appears at most twice, return an array of all the integers that appears twice.

Note: You can return the elements in any order but the driver code will print them in sorted order.

Examples:

Input: arr[] = [2, 3, 1, 2, 3]
Output: [2, 3] 
Explanation: 2 and 3 occur more than once in the given array.

Input: arr[] = [3, 1, 2] 
Output: []
Explanation: There is no repeating element in the array, so the output is empty.

_____________________________________________________________________________________________________________________________________________________________________________________

class Solution:
    def findDuplicates(self, arr):
        seen = set()
        duplicates = set()
        
        for num in arr:
            if num in seen:
                duplicates.add(num)
            else:
                seen.add(num)
        
        # If duplicates exist, return sorted list; otherwise, return empty list
        return sorted(list(duplicates))
