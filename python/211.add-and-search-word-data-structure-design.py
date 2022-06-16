#
# @lc app=leetcode id=211 lang=python3
#
# [211] Add and Search Word - Data structure design
#

# @lc code=start
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        root = self.root
        for w in word:
            root = root.children[w]
        root.isWord = True
    
    def search(self, root, word):
        for i in range(len(word)):
            if word[i] != '.':
                if word[i] in root.children:
                    root = root.children[word[i]]
                else:
                    return False
            else:
                for child in root.children:
                    if self.search(root.children[child], word[i+1:]):
                        return True
                return False
        return root.isWord


class WordDictionary(object):
    def __init__(self):
        self.trie = Trie()
        self.root = self.trie.root

    def addWord(self, word):
        self.trie.insert(word)
    
    def search(self, word):
        return self.trie.search(self.root, word)       


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

