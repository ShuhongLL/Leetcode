class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        worker_choice = {}
        num_workers = len(workers)
        for i, worker in enumerate(workers):
            choices = []
            for j, bike in enumerate(bikes):
                choices.append((self.dist(worker, bike), j))
                choices.sort()
            worker_choice[i] = choices[:num_workers]
        return self.dp(0, 0, set(), worker_choice, {})
           
    def dp(self, worker_i: int, cur_sum: int, seen_bikes: set, worker_choice:dict, memo: dict):
        # this 'sorted' is the key point
        seen_keys = tuple(sorted(list(seen_bikes)))
        if worker_i in memo and seen_keys in memo[worker_i]:
            return memo[worker_i][seen_keys]
        if worker_i >= len(worker_choice):
            return 0
        min_d = float('inf')
        for cur_d, bike_i in worker_choice[worker_i]:
            if bike_i in seen_bikes:
                continue
            seen_bikes.add(bike_i)
            next_min = self.dp(worker_i+1, cur_sum+cur_d, seen_bikes, worker_choice, memo)
            seen_bikes.remove(bike_i)
            min_d = min(min_d, next_min+cur_d)
        if worker_i not in memo:
            memo[worker_i] = {}
        memo[worker_i][seen_keys] = min_d
        return min_d
    
    def dist(self, worker: List[int], bike: List[int]):
            return abs(bike[0] - worker[0]) + abs(bike[1] - worker[1])