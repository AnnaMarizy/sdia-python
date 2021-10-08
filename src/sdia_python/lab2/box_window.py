import numpy as np

from sdia_python.lab2.utils import get_random_number_generator


class BoxWindow:
    """Class that creates BoxWindows in any dimension."""

    def __init__(self, bounds_args):  # ! naming: snake case for args
        """Initialize the BoxWindows from the bounds given in the array.

        Args:
            bounds_args (array or list): array (or list) of bounds containing the coordinates of each bound
        """
        bounds = np.array(bounds_args)
        a = bounds[:, 0]
        b = bounds[:, 1]
        # Test if the bounds given are correct ie a <= b
        assert np.all(a <= b), "The bounds given are incorrect"
        self.bounds = bounds

    def __str__(self):
        """Display the BoxWindow as a string
        Returns:
            string: BoxWindows points coordinates
        """
        # ! use f-strings
        # * consider a list comprehension
        description = "BoxWindow: "
        bounds_list = [f"{list(e)}" for e in self.bounds]
        sep = " x "
        return description + sep.join(bounds_list)

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
        ##Test if the point has the same dimension
        assert len(point) == self.dimension(), "The point has an incorrect dimension"

        a, b = self.bounds[:, 0], self.bounds[:, 1]
        # * could also combine np.all with and
        return np.all(a <= point) and np.all(point <= b)

    def dimension(self):
        """Gives the dimension of the BoxWindows"""
        return len(self)

    def volume(self):
        """Gives the volume of the BoxWindow

        Returns:
            int: volume
        """
        return np.prod(np.diff(self.bounds))

    def indicator_function(self, array_points):
        """Gives the result of the indicator function of the BoxWindows given some points of the same dimension

        Args:
            args (int): 1 if the argument is inside the BoxWindow, else 0
        """
        if array_points.ndim > 1:  # * use .ndim
            return np.array([p in self for p in array_points], dtype=int)
        return int(array_points in self)

    def rand(self, n=1, rng=None):
        """Generate ``n`` points uniformly at random inside a BoxWindow.

        Args:
            n (int, optional): Number of random points to generate. Defaults to 1.
            rng (seed, optional): Defaults to None.

        Returns: (n, d) array which contains n points randomly uniformly generated in a BoxWindow of dimension d
        """
        dim = self.dimension()
        rng = get_random_number_generator(rng)

        # * Nice use of numpy!
        a, b = self.bounds[:, 0], self.bounds[:, 1]
        points = rng.uniform(a, b, (n, dim))
        return points


class UnitBoxWindow(BoxWindow):
    def __init__(self, center):
        """Initialize a BoxWindow which is centered around the center given

        Args:
            center (array): coordinates of the center of the UnitBoxWindow
        """
        # ? how about np.add.outer
        # * Nice inlining
        bounds = np.add.outer(center, [-0.5, 0.5])
        super(UnitBoxWindow, self).__init__(bounds)
