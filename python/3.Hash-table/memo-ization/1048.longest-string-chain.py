import collections

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words = sorted(words, key = lambda x: len(x))
        memo = collections.defaultdict(int)
        s = set(words)
        result = 0
        for word in words:
            for i in range(len(word)):
                pre = word[:i] + word[i+1:]
                if pre not in s:
                    continue
                memo[word] = max(memo[word], memo[pre] + 1)
                result = max(result, memo[word])
        return result + 1
