import collections
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = collections.defaultdict(list)
        count = collections.defaultdict(int)
        queue = []
        result = 0
        
        # convert edge list to adjacency list
        for edge in prerequisites:
            pre[edge[1]].append(edge[0])
            count[edge[0]] += 1
        # find out the courses without any prerequisite
        for i in range(numCourses):
            if count[i] == 0:
                queue.append(i)
        # bfs
        while queue:
            result += 1
            node = queue.pop(0)
            for i in pre[node]:
                # node already seen
                if count[i] == 0:
                    continue
                count[i] -= 1
                if count[i] == 0:
                    queue.append(i)
        
        return result == numCourses
