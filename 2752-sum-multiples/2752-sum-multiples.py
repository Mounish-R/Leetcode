class Solution(object):
    def sumOfMultiples(self, n):
        """
        :type n: int
        :rtype: int
        """
        sums=0
        for i in range(n+1):
            if i%3==0:
                sums+=i
            elif i%5==0:
                sums+=i
            elif i%7==0:
                sums+=i
        return sums