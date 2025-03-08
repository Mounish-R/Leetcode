class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        clean=''
        for c in s:
            if c.isalnum():
                clean+=c.lower()
        return clean==clean[::-1]   