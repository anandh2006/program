You are given an integer n. Your task is to reverse the digits, ensuring that the reversed number has no leading zeroes.

Examples:

Input: n = 122
Output: 221
Explanation: By reversing the digits of number, number will change into 221.

_______________________________________________________________________________________________________________________________________________________________

class Solution:
    def reverseDigits(self, n):
        rev = str(n)[::-1]      # reverse the digits
        rev = rev.lstrip('0')   # remove leading zeros
        if rev == "":           # edge case: n = 0
            return 0
        return int(rev)         # return as integer
