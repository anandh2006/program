Given an array arr, write a program segregating even and odd numbers. The program should put all even numbers first in sorted order, and then odd numbers in sorted order.

Note:- You don't have to return the array, you have to modify it in-place.

Example:

Input: arr[] = [12, 34, 45, 9, 8, 90, 3]
Output: [8, 12, 34, 90, 3, 9, 45]
Explanation: Even numbers are 12, 34, 8 and 90. Rest are odd numbers.

_____________________________________________________________________________________________________________________________________________________________________________________________________


class Solution:

	def segregateEvenOdd(self,arr):
	    even = [x for x in arr if x % 2 == 0]
	    odd = [x for x in arr if x % 2 != 0]
	    even.sort()
	    odd.sort()
	    arr[:] = even+odd
	    
