# https://leetcode.com/problems/generate-random-point-in-a-circle/

'''
Given a circle with radius R and center at (a, b), write a function randPoint which generates a uniform random point inside the circle.

center = a, b
radius = R
range of X coordinates: [a-R, a+R]
range of Y coordinates: [b-R, b+R]

Formula for on the circle : (X - a)^2 + (Y - b)^2 == R^2
Formula for inside the circle : (X - a)^2 + (Y - b)^2 < R^2
Formula for outside the circle : (X - a)^2 + (Y - b)^2 > R^2

'''

import random
class Solution(object):

    def __init__(self, radius, x_center, y_center):
        """
        :type radius: float
        :type x_center: float
        :type y_center: float
        """
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

        self.x_min, self.x_max = x_center - radius, x_center + radius
        self.y_min, self.y_max = y_center - radius, y_center + radius

    def randPoint(self):
        """
        :rtype: List[float]
        """
        while True:
            x, y = random.uniform(self.x_min, self.x_max), random.uniform(self.y_min, self.y_max)
            if (x - self.x_center) ** 2 + (y - self.y_center) ** 2 <= self.radius ** 2:
                return [x, y]


print(Solution(1, 0, 0).randPoint())  # Example output: [0.5, -0.3]
print(Solution(10, 5, -7).randPoint())  # Example output: [3.2, -10.5]