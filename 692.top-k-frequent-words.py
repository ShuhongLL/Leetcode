#
# @lc app=leetcode id=692 lang=python3
#
# [692] Top K Frequent Words
#

# @lc code=start
import itertools

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words = sorted(words)
        l = [(len(list(group)), key) for key, group in itertools.groupby(words)]
        result =[item[1] for item in sorted(l, key = lambda x: [-x[0], x[1]])]
        return result[:k]
    # or
    # count = collections.Counter(word)
    # l = [(l, key) for key, l in count.items()]

# @lc code=end

