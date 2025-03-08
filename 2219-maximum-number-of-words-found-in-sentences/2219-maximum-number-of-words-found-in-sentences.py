class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        max_word=0
        for sentence in sentences:
            word=len(sentence.split())
            max_word=max(max_word,word)
        return max_word
        