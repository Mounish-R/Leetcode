class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        clean=''.join(c.lower() for c in s if c.isalnum())
        return clean==clean[::-1]