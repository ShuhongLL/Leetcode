import itertools

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        name_count = [(key, len(list(group))) for key, group in itertools.groupby(name)]
        typed_count = [(key, len(list(group))) for key, group in itertools.groupby(typed)]
        if len(name_count) != len(typed_count):
            return False
        for i in range(len(name_count)):
            if typed_count[i][0] != name_count[i][0]:
                return False
            if typed_count[i][1] < name_count[i][1]:
                return False
        return True
