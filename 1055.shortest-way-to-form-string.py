class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        count = 0
        cur = source
        while len(target) > 0:
            if target[0] not in source:
                return -1
            if target[0] == cur[0]:
                target, cur = target[1:], cur[1:]
            else:
                cur = cur[1:]
            if len(cur) == 0:
                count += 1
                cur = source
        return count+1 if cur != source and len(cur) != 0 else count
