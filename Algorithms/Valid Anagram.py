class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sl = list(s)
        tl = list(t)
        sl.sort()
        tl.sort()
        s = ''.join(sl)
        t = ''.join(tl)
        return s == t