class Solution(object):
    def answerString(self, word, numFriends):
        """
        :type word: str
        :type numFriends: int
        :rtype: str
        """
        if numFriends == 1:
            return word
        n = len(word)
        size = n - numFriends + 1
        max = word[0:size]
        
        """iterate through array, continue if the longest is smaller than max"""
        for i in range(len(word)):
            if word[i] < max[0]:
                continue
            lim = size if i + size <= n else n - i
            for j in range(lim, 0, -1):
                if max >= word[i:i+j]:
                    break
                if max < word[i:i+j]:
                    max = word[i:i+j]
        return max