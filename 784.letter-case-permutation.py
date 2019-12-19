class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        self.result = set()
        self.back_tracking(S.lower(), '')
        return list(self.result)
        
    def back_tracking(self, s: str, path: str):
        if not s:
            self.result.add(path)
        else:
            self.back_tracking(s[1:], path + s[0])
            self.back_tracking(s[1:], path + s[0].upper())
