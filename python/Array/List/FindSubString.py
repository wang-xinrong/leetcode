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

    def findSubstring_faster(self, s: str, words: List[str]) -> List[int]:
        word_dict = Counter(words)
        word_size = len(words[0])
        res = []
        for i in range(word_size):
            words_used=0
            words_found=defaultdict(int)
            start=i
            for j in range(i, len(s) - word_size + 1, word_size):
                new_word=s[j:j+word_size]

                if new_word not in word_dict:
                    # the loop has to restart
                    start=j+word_size
                    words_used=0
                    words_found=defaultdict(int)
                    continue

                # the current word is valid, we update relevant variables
                words_used+=1
                words_found[new_word]+=1
                while words_found[new_word] > word_dict[new_word]:
                    words_found[s[start:start+word_size]]-=1
                    start+=word_size
                    words_used-=1

                if words_used == len(words):
                    res.append(start)

        return res