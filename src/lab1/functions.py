def is_unique(x):
    """Returns True if there is no duplicate in x, otherwise return False

    Args:
        x (list): A list of elements

    Returns:
        bool: indicate if there is no duplicate in the list given
    """
    return len(set(x)) == len(x)


def triangle_shape(height):
    """Print a pyramid made of "x"

    Args:
        height (int): The height of the pyramid

    Returns:
        str: a string representing the pyramid, made with the character "x"
    """

    pyramid = ""
    if height == 0:
        return pyramid
    for i in range(height):
        pyramid += (
            (height - i - 1) * " " + (2 * i + 1) * "x" + (height - i - 1) * " " + "\n"
        )
    return pyramid[:-1]
