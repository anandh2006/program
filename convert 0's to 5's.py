class Solution:
    def convertFive(self, n):
        # Convert to string, replace all '0' with '5'
        return int(str(n).replace('0', '5'))
