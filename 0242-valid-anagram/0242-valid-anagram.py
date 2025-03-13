class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s=''.join(char.lower() for char in s if char.isalpha())
        t=''.join(char.lower() for char in t if char.isalpha())
        if Counter(s) == Counter(t):
            return True
        else:
            return False    