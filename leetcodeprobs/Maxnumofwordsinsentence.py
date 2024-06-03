class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        count=0
        for i in range(len(sentences)):
            words = sentences[i].split(" ")
            count =max(len(words),count)
        return count
