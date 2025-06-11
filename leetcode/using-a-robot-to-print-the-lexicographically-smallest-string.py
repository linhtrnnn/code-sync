class Solution(object):
    def robotWithString(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import Counter

        freq = Counter(s)

        t = []
        p = []

        n = len(s)

        def minChar():
            for i in range(26): 
                if freq[chr(ord('a') + i)] > 0:
                    return chr(ord('a') + i)
            return 'a'

        small = minChar() 
        for i in (range(n)):
            while t and t[-1] <= small:
                p.append(t.pop())

            t.append(s[i])
            freq[s[i]] -= 1

            if freq[small] == 0:
                small = minChar()

        while t:
            p.append(t.pop())
            

        return "".join(p)