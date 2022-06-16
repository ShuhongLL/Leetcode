import collections

class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        count = collections.defaultdict(int)
        queue = []
        construct = []
        
        # build edge A to B if A is in front of B
        for seq in seqs:
            for i, num in enumerate(seq):
                if num not in graph:
                    graph[num] = []
                if i < len(seq)-1:
                    graph[num].append(seq[i+1])
                    count[seq[i+1]] += 1

        # start with a node which has no parent        
        for key in graph:
            if count[key] == 0:
                queue.append(key)
        
        while queue:
            node = queue.pop()
            construct.append(node)
            for child in graph[node]:
                count[child] -= 1
                if count[child] == 0:
                    queue.append(child)
            # ensure there is only one result by checking len(queue) is always 1
            if len(queue) > 1:
                return False

        # note: constructed subseq has to contain every key(num) in graph
        return construct == org and len(construct) == len(graph)
