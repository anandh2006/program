Given a number n, return an array containing the first n Fibonacci numbers.

Note: The first two numbers of the series are 0 and 1.

Examples:

Input: n = 5
Output: [0, 1, 1, 2, 3]

________________________________________________________________________________________________________

class Solution:

    def fibonacciNumbers(self, n):

        if n <= 0:
            return []

        fib = [0, 1]

        for i in range(2, n):
            fib.append(fib[-1] + fib[-2])

        return fib[:n]
