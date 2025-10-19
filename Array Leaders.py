You are given an array arr of positive integers. Your task is to find all the leaders in the array. 
An element is considered a leader if it is greater than or equal to all elements to its right. The rightmost element is always a leader.

Examples:

Input: arr = [16, 17, 4, 3, 5, 2]
Output: [17, 5, 2]
Explanation: Note that there is nothing greater on the right side of 17, 5 and, 2.

____________________________________________________________________________________________________________________________________________________________________________________

class Solution:
    def leaders(self, arr):
        n = len(arr)
        new = []
        
        # Check each element if it's greater than all elements to its right
        for i in range(n):
            is_leader = True
            for j in range(i + 1, n):
                if arr[j] > arr[i]:
                    is_leader = False
                    break
            if is_leader:
                new.append(arr[i])
        
        return new
___________________________________________________________________________________________________________________________________________________________________________________

class Solution:
    def leaders(self, arr):
        n = len(arr)
        new = []
        
        # Start from the last element — it's always a leader
        max_from_right = arr[-1]
        new.append(max_from_right)
        
        # Traverse from right to left
        for i in range(n - 2, -1, -1):
            if arr[i] >= max_from_right:
                max_from_right = arr[i]
                new.append(arr[i])
        
        # Reverse to maintain original order
        new.reverse()
        return new

