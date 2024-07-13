from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or (not s) or (not t):
            return ''
        
        start, end = 0, 0
        count = len(t)
        dict = Counter(t)
        minlen = float('inf')
        res=[start,end]
        found=False

        while (end < len(s)):
            
            while (count > 0 and end < len(s)):
                if dict[s[end]] > 0:
                    count-=1
                dict[s[end]]-=1
                end+=1
            
            # start and end has been set based on start
            # to contain all char in dict, count should now
            # be 0


            
            # now i want to move start to the right such that for
            # count is positive again

            while (count == 0):
                found = True
                if s[start] in t:
                    if dict[s[start]] >= 0:
                        count+=1
                    dict[s[start]]+=1
                start+=1

            if (end - start + 1 < minlen):
                minlen = end - start + 1
                res[0]=start - 1
                res[1]=end
        
        return s[res[0]:res[1]] if found else ""
    
    def minWindowFaster(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        map = [0] * 128
        count = len(t)
        start = 0
        end = 0
        min_len = float('inf')
        start_index = 0
        # UPVOTE !
        for char in t:
            map[ord(char)] += 1

        while end < len(s):
            if map[ord(s[end])] > 0:
                count -= 1
            map[ord(s[end])] -= 1
            end += 1

            while count == 0:
                if end - start < min_len:
                    start_index = start
                    min_len = end - start

                if map[ord(s[start])] == 0:
                    count += 1
                map[ord(s[start])] += 1
                start += 1

        return "" if min_len == float('inf') else s[start_index:start_index + min_len]