class Solution:
    # 4 points form a square if and only if 
    # the distances (or squared distances) between the 6 pairs have exactly 2 non-zero values
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        points = [p1, p2, p3, p4]
        edge = set()
        for i in range(0, 3):
            for j in range(i+1, 4):
                l = (points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2
                if l == 0:
                    return False
                edge.add(l)
        return len(edge) == 2
