Given an array arr[] of positive integers. Return true if all the array elements are palindrome otherwise, return false.
Input: arr[] = [121, 131, 20]
Output: false
Explanation: 20 is not a palindrome hence the output is false.

___________________________________________________________________________________________________________________________________________________

def isPalinArray(arr):
    for i in arr:
        n = str(i)
        if n != n[::-1]:   # if any element is NOT palindrome
            return False
    return True            # all elements are palindrome
