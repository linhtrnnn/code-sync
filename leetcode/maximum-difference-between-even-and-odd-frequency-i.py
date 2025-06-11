class Solution(object):
    def maxDifference(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
        freq = Counter(s)
        maxOdd = -float('inf')
        minEven = float('inf')
        for count in freq.values():
            if count % 2 == 1:
                if count > maxOdd:
                    maxOdd = count
            else:
                if count < minEven and count > 0:
                    minEven = count
        return maxOdd - minEven