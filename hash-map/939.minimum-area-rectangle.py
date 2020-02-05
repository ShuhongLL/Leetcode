class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        memo = set(map(tuple, points))
        result = float('inf')
        for i in range(len(points)):
            x, y = points[i]
            for j in range(i+1, len(points)):
                a, b = points[j]
                if x == a or y == b:
                    continue
                if (a, y) not in memo or (x, b) not in memo:
                    continue
                width = abs(x - a)
                height = abs(y - b)
                result = min(result, width*height)
        return result if result != float('inf') else 0
