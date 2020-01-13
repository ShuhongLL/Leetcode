import collections
class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.width = width
        self.height = height
        self.score = 0
        self.food = food
        self.f = 0
        self.head = (0, 0)
        self.body = collections.deque([(0, 0)])
        self.direct = {
            'D': (1, 0),
            'L': (0, -1),
            'R': (0, 1),
            'U': (-1, 0)
        }
        

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        a, b = self.head[0] + self.direct[direction][0], self.head[1] + self.direct[direction][1]
        # collide with border
        if a < 0 or b < 0 or a >= self.height or b >= self.width:
            return -1
        # eat the food
        if self.f < len(self.food) and a == self.food[self.f][0] and b == self.food[self.f][1]:
            self.score += 1
            self.f += 1
            self.head = (a, b)
            self.body.append(self.head)
            return self.score
        # collide with body
        if (a, b) in self.body and self.body[0] != (a, b):
            return -1
        # move one step further
        self.head = (a, b)
        self.body.append(self.head)
        self.body.popleft()
        return self.score


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)