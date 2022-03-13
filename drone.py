# Nakarin Philangam
# 1/25/2022

class Drone:

    def __init__(self):
        self.speed = 0.0
        self.height = 0.0

    def accelerate(self):
        self.speed += 10

    def decelerate(self):
        # Can not be negative
        if self.speed < 10:
            self.speed = 0
        else:
            self.speed -= 10

    def ascend(self):
        self.height += 10

    def descend(self):
        # Can not be negative
        if self.height < 10:
            self.height = 0
        else:
            self.height -= 10
