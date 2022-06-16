import collections
import heapq

class Node:
    def __init__(self):
        self.isWord = False
        self.nodes = collections.defaultdict(Node)
        self.suggest = []
        
        
class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word: str):
        cur = self.root
        for char in word:
            cur = cur.nodes[char]
            heapq.heappush(cur.suggest, word)
        cur.isWord = True
    
    def query(self, word: str):
        result = []
        cur = self.root
        for i in range(len(word)):
            if word[i] not in cur.nodes:
                return result + [[] for _ in range(len(word) - i)]
            cur = cur.nodes[word[i]]
            val = []
            while cur.suggest and len(val) < 3:
                val.append(heapq.heappop(cur.suggest))
            result.append(val)
        return result
                

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for product in products:
            trie.insert(product)
        return trie.query(searchWord)
