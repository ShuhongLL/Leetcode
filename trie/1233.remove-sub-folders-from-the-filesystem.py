import collections

class TrieNode:
    def __init__(self):
        self.nodes = collections.defaultdict(TrieNode)
        self.isDir = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, names: List[str]):
        cur = self.root
        for name in names:
            if cur.isDir:
                return False
            cur = cur.nodes[name]
        cur.isDir = True
        cur.nodes = {}
        return True
    
    def traversal(self):
        validDir = []
    
        def dfs(node: TrieNode, path: str):
            if node.isDir:
                validDir.append(path)
                return
            for name in node.nodes:
                dfs(node.nodes[name], path + '/' + name)
        
        dfs(self.root, '')
        return validDir


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        for path in folder:
            names = path.split('/')
            trie.insert(names[1:])
        return trie.traversal()
