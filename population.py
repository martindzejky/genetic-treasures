import inset


def generate(size=100):
    """Generate a population of random insets."""

    return tuple(inset.generate() for i in range(size))
