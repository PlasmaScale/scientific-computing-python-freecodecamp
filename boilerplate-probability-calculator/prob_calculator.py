import random
import copy

class Hat:

    def __init__(self, **kwargs):
        self.contents = []
        for key in kwargs:
            for i in range(kwargs[key]):
                self.contents.append(key)

    def draw(self, num_balls):
        draw = []
        if num_balls > len(self.contents):
            return self.contents
        while num_balls > 0:
            random_number = random.randint(0, len(self.contents)-1)
            random_ball = self.contents.pop(random_number)
            draw.append(random_ball)
            num_balls -= 1
        return draw

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pos_outcomes = 0
    num_of_draws = num_experiments
    while num_of_draws > 0:
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        same_num_balls = sum([drawn_balls.count(ball) >= expected_balls[ball] for ball in expected_balls])
        if same_num_balls == len(expected_balls):
            pos_outcomes += 1
        num_of_draws -= 1
    return pos_outcomes/num_experiments


