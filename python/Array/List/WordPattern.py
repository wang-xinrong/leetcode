class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        for i in range(len(pattern)):
            if pattern.index(pattern[i]) != words.index(words[i]):
                return False
        return True
    def wordPatternFaster(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if (len(words) != len(pattern)):
            return False
        combined_set = set(zip(pattern, words))
        return len(combined_set) == len(set(pattern)) == len(set(words))
        