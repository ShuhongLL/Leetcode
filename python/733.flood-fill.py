class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int, preColor: int = None) -> List[List[int]]:
        steps = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        color = image[sr][sc]
        if not preColor:
            preColor = color
        image[sr][sc] = float('inf')
        for dx, dy in steps:
            a, b = sr + dx, sc + dy
            if a >= 0 and a < len(image) and b >= 0 and b < len(image[0]) and image[a][b] == preColor:
                self.floodFill(image, a, b, newColor, preColor)
        image[sr][sc] = newColor
        return image
