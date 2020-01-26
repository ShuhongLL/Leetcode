class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # sort by hour-minute
        time = sorted(timePoints, key = lambda s: [s[0:2], s[3:5]])
        # to compare head and tail
        time.append(f'{int(time[0][0:2])+24}:{time[0][3:5]}')
        minDif = float('inf')
        for i in range(1, len(time)):
            if time[i-1][0:2] < time[i][0:2]:
                h = int(time[i][0:2]) - int(time[i-1][0:2])
                offset = int(time[i][3:5]) + 60 - int(time[i-1][3:5])
                minDif = min(minDif, (h-1)*60 + offset)
            else:
                minDif = min(minDif, int(time[i][3:5]) - int(time[i-1][3:5]))
        return minDif
