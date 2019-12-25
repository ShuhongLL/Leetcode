import itertools

class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        # Method: Ordered map
        hand_s = sorted(hand)
        memo = {}
        for key, group in itertools.groupby(hand_s):
            memo[key] = len(list(group))
        for key in memo:
            val = memo[key]
            if val == 0:
                continue
            if val < 0:
                return False
            for i in range(1, W):
                if key+i in memo:
                    memo[key+i] -= val
                else:
                    return False
        return True
