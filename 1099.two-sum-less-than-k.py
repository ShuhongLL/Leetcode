class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        # method 1: Brute Force
        # result = 0
        # for i in range(len(A) - 1):
        #     for j in range(i+1, len(A)):
        #         cur = A[i] + A[j]
        #         result = max(cur, result) if cur < K else result
        # return result if result != 0 else -1
        
        # method 2: Two Pointer
        if len(A) < 2:  return -1
        A = sorted(A)
        l, r = 0, len(A)-1
        result = 0

        while l < r:
            cur = A[l] + A[r]
            if cur < K:
                result = max(result, cur)
                l += 1
            else:
                r -= 1
        return result if result != 0 else -1
