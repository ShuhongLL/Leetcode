class Solution:

    # Method 1: memoization, Memory Limit Exceeded !

    # def findLength(self, A: List[int], B: List[int]) -> int:
    #     memo = {}
    #     result = 0
    #     for i in range(len(A)):
    #         if (i, i) not in memo:  memo[i, i] = set()
    #         for v in [(p, p) for p, v in enumerate(B) if v == A[i]]:
    #             memo[i, i].add(v)
    #         if len(memo[i, i]) != 0:    result = 1
    #     for l in range(1, len(A)):
    #         for head in range(0,  len(A)-l):
    #             tail = head + l
    #             if (head, tail-1) not in memo:
    #                 continue
    #             for v in memo[head, tail-1]:
    #                 start, end = v[0], v[1]
    #                 if end+1 < len(B) and B[end+1] == A[tail]:
    #                     if (head, tail) not in memo:    memo[head, tail] = set()
    #                     memo[head, tail].add((start, end+1))
    #                     result = max(result, l+1)
    #     return result
    
    # method 2: dp
    def findLength(self, A: List[int], B: List[int]) -> int:
        dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
        for i in range(len(A)-1, -1, -1):
            for j in range(len(B)-1, -1, -1):
                if A[i] == B[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
        return max(max(row) for row in dp)
