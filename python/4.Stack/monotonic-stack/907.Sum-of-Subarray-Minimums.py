class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        """
        end of the arr: [-1, len(arr)]
        value = arr[i] * (i - l_i) * (r_i - i)
        e.g. [1,2] = 1*2 + 2
             result for 1 is 1 * (0 - -1) * (2 - 0) = 2
        """
        stack = []
        lresult = [0] * len(arr)
        for i in range(len(arr)):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop(-1)
            lresult[i] = stack[-1] if stack else -1
            stack.append(i)
        
        stack = []
        rresult = [0] * len(arr)
        for i in range(len(arr)-1, -1, -1):
            # note: no equal sign here
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop(-1)
            rresult[i] = stack[-1] if stack else len(arr)
            stack.append(i)

        ans = 0
        d = 10**9 + 7
        for i in range(len(arr)):
            val = arr[i] * (i - lresult[i]) * (rresult[i] - i)
            ans = (ans + val) % d
        return ans
        