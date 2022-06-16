import itertools

class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        # Method: Ordered map
        hand = sorted(hand)
        memo = {key: len(list(group)) for key, group in itertools.groupby(hand)}
        
        for card in memo:
            val = memo[card]
            if val == 0:
                continue
            if val < 0:
                return False
            for i in range(1, W):
                if card+i in memo:
                    memo[card+i] -= val
                else:
                    return False
        return True
