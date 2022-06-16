import collections

class Solution:
#     method 1: bfs Time Limit Exceed !
#     def canTransform(self, start: str, end: str) -> bool:
#         queue = collections.deque([])
#         queue.append(start)
#         seen = {}
#         while queue:
#             node = queue.popleft()
#             if node == end:
#                 return True
#             if node in seen:
#                 continue
#             seen[node] = None
#             queue += self.shift(node)
#         return False
            
#     def shift(self, s: List[str], start: int = 1):
#         result = []
#         for i in range(start, len(s)):
#             if s[i-1:i+1] == 'XL':
#                 result += self.shift(s[:i-1] + 'LX' + s[i+1:], i+1)
#             elif s[i-1:i+1] == 'RX':
#                 result += self.shift(s[:i-1] + 'XR' + s[i+1:], i+1)
#         result.append(s)
#         return result

#   method 2: Two Pointers
#   observe that:
#   'XL' -> 'LX'  moves 'L' to the left
#   'RX' -> 'XR'  moves 'R' to the right
#   the order of 'L' and 'R' keeps invariant

#   In additions:
#   The index of each 'L' in start should always be on the left of the final end string
#   Since 'L's can obly be moved to be left
#   same as 'R'

    def canTransform(self, start: str, end: str) -> bool:
        if start.replace('X', '') != end.replace('X', ''):
            return False
        s_R = e_R = s_L = e_L = 0
        for i in range(len(start)):
            if start[i] == 'R':
                s_R += 1
            if end[i] == 'R':
                e_R += 1
            if start[i] == 'L':
                s_L += 1
            if end[i] == 'L':
                e_L += 1
            if s_R < e_R:
                return False
            if s_L > e_L:
                return False
        return s_R == e_R and s_L == e_L
  