from heapq import heapify, heappush, heappop

class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        def dist(worker: List[int], bike: List[int]):
            return abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])
        
        heap = []
        memo = [[] for _ in range(len(workers))]
        answer, seen_bikes = [None]*len(workers), set()
        for i, worker in enumerate(workers):
            for j, bike in enumerate(bikes):
                memo[i].append((dist(worker, bike), i, j))
        
        for i in range(len(memo)):
            heapify(memo[i])
            heappush(heap, heappop(memo[i]))
            
        while len(seen_bikes) < len(workers):
            _, worker, bike = heappop(heap)
            if bike in seen_bikes:
                heappush(heap, heappop(memo[worker]))
            else:
                answer[worker] = bike
                seen_bikes.add(bike)
        return answer
