class SnapshotArray:
    def __init__(self, length: int):
        # not need to init list to save memory
        self.nums = {}
        self.snaps = []

    def set(self, index: int, val: int) -> None:
        self.nums[index] = val

    def snap(self) -> int:
        self.snaps.append(self.nums.copy())
        return len(self.snaps)-1

    def get(self, index: int, snap_id: int) -> int:
        return self.snaps[snap_id][index] if index in self.snaps[snap_id] else 0


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)