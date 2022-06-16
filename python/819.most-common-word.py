#
# @lc app=leetcode id=819 lang=python3
#
# [819] Most Common Word
#

# @lc code=start
import itertools
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.sub('[^\w\s]+', ' ', paragraph).lower().split(' ')
        words = [i for i in words if i]
        seen = [(key, len(list(group))) for key, group in itertools.groupby(sorted(words))]
        seen = sorted(seen, key = lambda x : -x[1])
        for key, _ in seen:
            if key not in banned:
                return key
        return ""

# @lc code=end

