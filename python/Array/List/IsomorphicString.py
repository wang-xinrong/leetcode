class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        zipped_set = set(zip(s, t))
        return len(zipped_set) == len(set(s)) == len(set(t))
    def isIsomorphicAlternative(self, s: str, t: str) -> bool:
        s_to_t = dict()

        if len(s) != len(t): return False
        if len(set(s)) != len(set(t)): return False
        for i in range(len(s)):
            if s[i] not in s_to_t: 
                s_to_t[s[i]] = t[i]
            elif s_to_t[s[i]] != t[i]: 
                return False

        return True