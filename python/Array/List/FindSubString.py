from typing import List
from collections import Counter, defaultdict

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ws = len(words)*len(words[0])
        result = []
        localdict={}

        for word in words:
                if localdict.get(word) is not None:
                    localdict[word]+=1
                else:
                    localdict[word]=1

        for i in range(len(s) - ws + 1):
            dict = localdict.copy()
            window = s[i:i+ws]
            success=True
            for j in range(0, ws, len(words[0])):
                piece = window[j:j+len(words[0])]
                query = dict.get(piece)
                if query is None or query == 0:
                    success = False
                    break
                else:
                    dict[piece]-=1
            if success:
                result.append(i)
            
        return result

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        length = len(words[0])
        word_count = Counter(words)
        indexes = []

        for i in range(length):
            start = i
            window = defaultdict(int)
            words_used = 0

            for j in range(i, len(s) - length + 1, length):
                word = s[j:j + length]

                if word not in word_count:
                    start = j + length
                    window = defaultdict(int)
                    words_used = 0
                    continue

                words_used += 1
                window[word] += 1

                while window[word] > word_count[word]:
                    window[s[start:start + length]] -= 1
                    start += length
                    words_used -= 1

                if words_used == len(words):
                    indexes.append(start)

        return indexes

