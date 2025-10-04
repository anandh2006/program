Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.

Note: The second largest element should not be equal to the largest element.

Examples:

Input: arr[] = [12, 35, 1, 10, 34, 1]
Output: 34
Explanation: The largest element of the array is 35 and the second largest element is 34.

________________________________________________________________________________________________________________________________________________________

class Solution:
    def getSecondLargest(self, arr):
        if len(arr) < 2:
            return None   

        first = second = float('-inf')
        for num in arr:
            if num > first:         
                second = first
                first = num
            elif num > second and num < first:   
                second = num

        return second if second != float('-inf') else -1
