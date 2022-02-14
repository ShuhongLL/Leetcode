import itertools

class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        t_count = [(key, len(list(group))) for key, group in itertools.groupby(S)]
        result = 0
        for word in words:
            cur_count = [(key, len(list(group))) for key, group in itertools.groupby(word)]
            if len(cur_count) != len(t_count):
                continue
            for i in range(len(t_count)):
                if cur_count[i][0] != t_count[i][0]:
                    break
                if t_count[i][1] != cur_count[i][1]:
                    if t_count[i][1] < 3 or cur_count[i][1] > t_count[i][1]:
                        break
            else:
                result += 1
        return result