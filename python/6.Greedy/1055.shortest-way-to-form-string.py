class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        sp, tp = 0, 0
        count = 0
        memo = set(map(str, source))
        while tp < len(target):
            if target[tp] not in memo:
                return -1
            if source[sp] == target[tp]:
                tp += 1
            sp += 1

            if sp == len(source):
                sp = 0
                count += 1
        # by the time the above loop finish
        # sp may not reach the end of source
        # hence need to check if sp
        return count if sp == 0 else count+1
