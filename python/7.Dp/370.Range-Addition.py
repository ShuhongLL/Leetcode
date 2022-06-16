class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        """
        DP:
            apply [1,3,2]:
            0  0  0  0  0
          ->0  2  0  0 -2
              +2 --------|
                       -2|
                       
            apply [2,4,3]:
            0  2  0  0 -2
          ->0  2  3  0 -2
                 +3------|
                 
            apply [0,2,-2]:
            0  2  3  0 -2
         ->-2  2  3  2 -2
           -2------------|
                    +2---|
        """
        result = [0] * length
        for start, end, val in updates:
            result[start] += val
            if end < length - 1:
                result[end+1] -= val
        
        for i in range(1, length):
            result[i] += result[i-1]
        
        return result
