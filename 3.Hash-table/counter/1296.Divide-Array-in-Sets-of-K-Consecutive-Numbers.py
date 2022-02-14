import collections

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        count = collections.Counter(nums)
        nums_s = sorted(nums)
        for num in nums_s:
            if count[num] == 0:
                continue
            for i in range(k):
                if num+i in count and count[num+i] > 0:
                    count[num+i] -= 1
                else:
                    return False
        return True
