#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#
class Solution:
    def simplifyPath(self, path: str) -> str:
        
        def canonicalPath(paths: List[str], canPath: List[str]):
            if not paths:
                return canPath
            path = paths[0]

            if path == "":
                return canonicalPath(paths[1:], canPath)
            elif path == ".":
                return canonicalPath(paths[1:], canPath)
            elif path == "..":
                size = len(canPath)
                return canonicalPath(paths[1:], canPath[0 : size - 1])
            else:
                return canonicalPath(paths[1:], canPath + [path])

        canonicalPath = canonicalPath(path.split('/'), [])
        return '/' + '/'.join(canonicalPath)
            

