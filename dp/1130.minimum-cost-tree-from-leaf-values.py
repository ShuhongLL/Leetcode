class Solution:  
    def mctFromLeafValues(self, arr: List[int]) -> int:
        # build tree from bottom up
        # dp solution
        memo = {}
        for i in range(len(arr)):
            memo[i, i] = 0
        for l in range(1, len(arr)):
            for head in range(0, len(arr) - l):
                tail = head + l
                if (head, tail) not in memo:
                    memo[head, tail] = float('inf')
                for i in range(head, tail):
                    cur = max(arr[head:i+1]) * max(arr[i+1:tail+1]) + memo[head, i] + memo[i+1, tail]
                    memo[head, tail] = min(memo[head, tail], cur)
        return memo[0, len(arr)-1]
