import collections

class Solution(object):
    def isAnagram(self, s, t):
        counter1 = collections.Counter(s)
        counter2 = collections.Counter(t)
        return counter1 == counter2