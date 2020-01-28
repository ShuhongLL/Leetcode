import collections

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        queue = []
        for ast in asteroids:
            while queue and ast < 0 < queue[-1]:
                if queue[-1] < -ast:
                    queue.pop()
                    continue
                elif queue[-1] == -ast:
                    queue.pop()
                break
            else:
                queue.append(ast)
        return queue
