from math import gamma  # * see also scipy.special
from random import random

import numpy as np
import numpy.linalg as la

from sdia_python.lab2.utils import get_random_number_generator


class BallWindow:
    """Creates a Ball window, meaning a volume around a center point with a radius"""

    def __init__(self, center, radius=1.0):
        """Initialize the BallWindows from the center and the radius

        Args:
            center (list) : Gives the coordinates of the center
            radius (float) : Gives the radius of the ball. Default to 1.
        """

        self.center = np.array(center)
        self.radius = radius

    def __str__(self):
        """Display the BallWindow as a string

        Returns:
            string: BallWindows center and radius
        """

        description = (
            f"BallWindow: center = {list(self.center)} & radius = {self.radius}"
        )
        return description

    def __len__(self):
        """Returns the dimension of the space of the BallWindow

        Returns:
            int: Size of the space containing the BallWindow
        """

        return self.center.size

    def __contains__(self, point):
        """Indicates whether the argument given is inside the Ball Window of not.
        Assertion error if the dimension of the point is not equal to the dimension of the BallWindow

        Args:
            point (np.array): [list of coordinates]

        Returns:
            boolean: True if the point is inside, else returns False
        """

        # ? readability: len(self) => self.dimension()
        assert (
            len(point) == self.dimension()
        )  ##Test if the point has the same dimension
        return la.norm(self.center - point) <= self.radius

    def dimension(self):
        """Gives the dimension of the BallWindows, see __len__

        Returns:
            int: The dimension of the BallWindow
        """

        return len(self)

    def volume(self):
        """Gives the volume of the BallWindow

        Returns:
            int: The volume of the BallWindow
        """
        n = self.dimension()
        R = self.radius
        return (np.pi ** (n / 2) * R ** (n)) / gamma(1 + n / 2)

    def indicator_function(self, array_points):
        """Gives the result of the indicator function of the BallWindows given some points of the same dimension

        Args:
            args ([int]): 1 if the argument is inside the BallWindow, else 0
        """
        # * same remarks as in BoxWindow.indicator_function
        if array_points.ndim > 1:
            return np.array([int(p in self) for p in array_points], dtype=int)
        return int(array_points in self)

    def rand(self, n=1, rng=None):
        """Generate ``n`` points uniformly at random inside the :py:class:`BallWindow`.

        Args:
            n (int, optional): Number of random points to generate. Defaults to 1.
            rng (type, optional): Defaults to None.

        Returns: Array which contains n points randomly uniformly generated

        """
        dim = self.dimension()
        r = self.radius
        rng = get_random_number_generator(rng)

        points_l = np.empty((n, dim))
        for index in range(n):
            # an array of dim normally distributed random variables
            u = np.random.normal(0, 1, dim)
            point_radius = r * random() ** (1.0 / dim)
            points_l[index] = np.reshape(point_radius * u / la.norm(u), (1, 2))
        return points_l + self.center
