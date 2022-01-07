class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0] * n for _ in range(n)]
        left, right, up, down = 0, n-1, 0, n-1
        num = 1
        
        while left < right and up < down:
            # 左开右闭
            for x in range(left, right):
                result[up][x] = num
                num += 1
            
            for y in range(up, down):
                result[y][right] = num
                num += 1
                
            for x in range(right, left, -1):
                result[down][x] = num
                num += 1
                
            for y in range(down, up, -1):
                result[y][left] = num
                num += 1
            
            # 缩小范围进入内圈
            left += 1
            right -= 1
            up += 1
            down -= 1
            
        # 奇数时需要填中心
        if n % 2 == 1:
            result[n//2][n//2] = num
            
        return result
