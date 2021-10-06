import numpy as np

from lab2.utils import get_random_number_generator


class BoxWindow:
    """Class that creates BoxWindows in any dimension."""

    def __init__(self, boundsArg):  # ! naming: snake case for args
        """Initialize the BoxWindows from the bounds given in the array.

        Args:
            boundsArg (array): array of bounds containing the coordinates of each bound
        """

        self.bounds = boundsArg

    def __str__(self):
        """Display the BoxWindow in a string
        # ? IN a string
        Returns:
            string: BoxWindows points coordinates
        """
        # ! use f-strings
        # * consider a list comprehension
        description = "BoxWindow: "
        for i in range(len(self.bounds)):
            description = description + str(list(self.bounds[i])) + " x "
        return description[:-3]

    def __len__(self):
        """Returns the dimension of the space of the BoxWindow

        Returns:
            int: size of the space containing the BoxWindow
        """
        return self.bounds.shape[0]

    def __contains__(self, point):
        """Indicates whether the argument given is inside the Box Window of not.
        Assertion error if the dimension of the point is not equal to the dimension of the BoxWindow

        Args:
            point (np.array): list of coordinates

        Returns:
            boolean: True if the point is inside, else returns False
        """
        # ? readability: == self.dimension()
        assert len(point) == len(self)  ##Test if the point has the same dimension

        a = self.bounds[:, 0]
        b = self.bounds[:, 1]
        # * could also combine np.all with and
        return np.all(np.logical_and(a <= point, point <= b))
        """
        #Solution that allows to stop as soon as we find a False
        dim = len(self)
        for i in range(dim):
            a = self.bounds[i, :]
            if a[0] > point[i] or a[1] < point[i]:
                return False
        return True"""

    def dimension(self):
        """Gives the dimension of the BoxWindows"""
        return len(self)

    def volume(self):
        """Gives the volume of the BoxWindow

        Returns:
            int: volume
        """
        a = self.bounds[:, 0]
        b = self.bounds[:, 1]
        # * use np.diff
        # ? why using abs, b should always be >= a, is this tested ?
        return np.prod(abs(b - a))

    def indicator_function(self, array_points):
        """Gives the result of the indicator function of the BoxWindows given some points of the same dimension

        Args:
            args (int): 1 if the argument is inside the BoxWindow, else 0
        """
        if len(array_points.shape) > 1:  # * use .ndim
            # * use np.array(, dtype=int)
            return np.array([int(p in self) for p in array_points])
        return int(array_points in self)

    def rand(self, n=1, rng=None):
        """Generate ``n`` points uniformly at random inside the :py:class:`BoxWindow`.

        Args:
            n (int, optional): Number of random points to generate. Defaults to 1.
            rng (type, optional): Defaults to None.

        # todo specify the dimension of the array
        Returns: array which contains n points randomly uniformly generated
        """
        dim = len(self)  # or self.dimension()
        rng = get_random_number_generator(rng)

        # * Nice use of numpy!
        a = self.bounds[:, 0]
        b = self.bounds[:, 1]
        res = rng.uniform(a, b, (n, dim))
        # ? naming: res -> points
        return res


class UnitBoxWindow(BoxWindow):
    def __init__(self, center, dimension):
        """Initialize a BoxWindow which is centered around the center given (default = 0)
        and in the dimension given (default = 2)

        Args:
            dimension ([int]): dimension expected of the BoxWindow
            center ([type], optional): . Defaults to None.
        """
        # ? how about np.add.outer
        bounds = np.zeros((dimension, 2))
        # * Nice inlining
        bounds[:, 0], bounds[:, 1] = center - 0.5, center + 0.5
        super(UnitBoxWindow, self).__init__(bounds)
