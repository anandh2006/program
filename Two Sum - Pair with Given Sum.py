Given an array arr[] of integers and another integer target. Determine if there exist two distinct indices such that the sum of their elements is equal to the target.

Examples:

Input: arr[] = [0, -1, 2, -3, 1], target = -2
Output: true
Explanation: arr[3] + arr[4] = -3 + 1 = -2

______________________________________________________________________________________________________________________________________________________________

class Solution:
    def twoSum(self, arr, target):
        seen = set()  # store numbers we've seen so far
        for num in arr:
            complement = target - num  # what number we need
            if complement in seen:  # if we've seen it already
                return True
            seen.add(num)  # add current number for future
        return False
