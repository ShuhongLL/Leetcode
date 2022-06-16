class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        length = len(cardPoints) - k
        cur = sum(cardPoints[:length])
        result = cur
        for r in range(length, len(cardPoints)):
            cur += (cardPoints[r] - cardPoints[r-length])
            result = min(result, cur)
        return sum(cardPoints) - result
