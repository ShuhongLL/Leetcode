import collections

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if not nums:
            return 0
        
        # Monotonic Queues
        maxQ, minQ = collections.deque([0]), collections.deque([0])
        l = 0
        result = 1
        # Sliding Window
        for r in range(1, len(nums)):
            while maxQ and nums[maxQ[-1]] < nums[r]:
                maxQ.pop()
            maxQ.append(r)
            while minQ and nums[minQ[-1]] > nums[r]:
                minQ.pop()
            minQ.append(r)
            
            while maxQ and minQ and nums[maxQ[0]] - nums[minQ[0]] > limit:
                l += 1
                while maxQ[0] < l:
                    maxQ.popleft()
                while minQ[0] < l:
                    minQ.popleft()
                    
            result = max(result, r - l + 1)
        return result
