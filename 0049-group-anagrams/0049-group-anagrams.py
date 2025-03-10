class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram={}
        for s in strs:
            sort=''.join(sorted(s))
            if sort in anagram:
                anagram[sort].append(s)
            else:
                anagram[sort]=[s]
        return list(anagram.values())                   