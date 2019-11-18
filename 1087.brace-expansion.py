class Solution:
    def expand(self, S: str) -> List[str]:
        self.result = []
        self.dfs(S, "")
        return self.result
        
    def dfs(self, s:str, path: str):
        if not s:
            self.result.append(path)
            return
        if s[0] == '{':
            end = s.index('}')
            for char in sorted(s[1:end].split(',')):
                self.dfs(s[end+1:], path + char)
        else:
            self.dfs(s[1:], path + s[0])
