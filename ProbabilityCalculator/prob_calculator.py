import copy
import random


# Consider using the modules imported above.


class Hat:
    def __init__(self, **balls):
        self.contents = []
        for key, value in balls.items():
            for j in range(value):
                self.contents.append(key)

    def draw(self, ball_count):
        balls_removed = []
        if ball_count <= len(self.contents):
            for i in range(ball_count):
                random_ball_index = random.randrange(len(self.contents))
                balls_removed.append(self.contents[random_ball_index])
                del self.contents[random_ball_index]
            return balls_removed
        else:
            return self.contents


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expected_balls_list = []
    distinct_expected_ball_types = list(expected_balls)
    prob_match = 0

    for key, value in expected_balls.items():
        for j in range(value):
            expected_balls_list.append(key)

    for draw_experiment in range(num_experiments):
        copy_hat = copy.deepcopy(hat)
        ball_drawn_list = copy_hat.draw(num_balls_drawn)

        if all(ball in ball_drawn_list and ball_drawn_list.count(ball) >= expected_balls_list.count(ball) for ball in distinct_expected_ball_types):
            prob_match += 1
        ball_drawn_list.clear()

    return prob_match / num_experiments
