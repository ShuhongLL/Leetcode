class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # greedy algorithm
        boxes = sorted(boxTypes, key = lambda x: -x[1])
        remain = truckSize
        max_unit = 0
        for num, unit in boxes:
            if num >= remain:
                max_unit += remain * unit
                break
            max_unit += num * unit
            remain -= num
        return max_unit
