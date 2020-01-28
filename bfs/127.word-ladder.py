#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start
import collections

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        dicts = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                dicts[word[:i] + '#' + word[i + 1:]].append(word)
        
        seen = set()
        queue = collections.deque([(beginWord, 1)])
        while queue:
            word, step = queue.popleft()
            if word == endWord: return step
            seen.add(word)
            for i in range(len(word)):
                for sibling in dicts[word[:i] + '#' + word[i + 1:]]:
                    if sibling not in seen:
                        queue.append((sibling, step + 1))
        return 0
# @lc code=end