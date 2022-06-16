#
# @lc app=leetcode id=636 lang=python3
#
# [636] Exclusive Time of Functions
#

# @lc code=start
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        result = [0 for _ in range(n)]
        stack = []
        # use a stack to tracking the task stack
        # prev is the timestamp of the previous operation
        for i in range(len(logs)):
            log = logs[i].split(':')
            if log[1] == 'start':
                if len(stack) > 0:
                    result[stack[-1]] += int(log[2]) - prev
                stack.append(int(log[0]))
                prev = int(log[2])
            elif log[1] == 'end':
                result[stack.pop()] += int(log[2]) - prev + 1
                prev = int(log[2]) + 1
        return result
        
# @lc code=end

