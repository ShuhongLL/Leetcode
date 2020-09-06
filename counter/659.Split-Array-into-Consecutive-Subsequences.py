import collections

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        count = collections.Counter(nums)
        tail = collections.Counter()
        for num in nums:
            if count[num] == 0:
                continue
            # prefer append to an existing list
            if tail[num] > 0:
                tail[num] -= 1
                tail[num + 1] += 1
            elif count[num+1] > 0 and count[num+2] > 0:
                count[num+1] -= 1
                count[num+2] -= 1
                tail[num+3] += 1
            else:
                return False
            count[num] -= 1
        return True
