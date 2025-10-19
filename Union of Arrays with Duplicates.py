You are given two arrays a[] and b[], return the Union of both the arrays in any order.

The Union of two arrays is a collection of all distinct elements present in either of the arrays. 
If an element appears more than once in one or both arrays, it should be included only once in the result.

Note: Elements of a[] and b[] are not necessarily distinct.
Note that, You can return the Union in any order but the driver code will print the result in sorted order only.

Examples:

Input: a[] = [1, 2, 3, 2, 1], b[] = [3, 2, 2, 3, 3, 2]
Output: [1, 2, 3]
Explanation: Union set of both the arrays will be 1, 2 and 3.

__________________________________________________________________________________________________________________________________________________________________


class Solution:    
    def findUnion(self, a, b):
        # code here
        s = []
        m = set(a)
        n = set(b)
        s = m.union(n)
        return s

__________________________________________________________________________________________________________________________________________________________________

class Solution:
    def findUnion(self, a, b):
        return set(a).union(set(b))

__________________________________________________________________________________________________________________________________________________________________

class Solution:
    def findUnion(self, a, b):
        return set(a + b)   

