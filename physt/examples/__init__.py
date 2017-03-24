"""A set of examples used for demonstrating the physt capabilities / in tests."""

import numpy as np
from ..import h1, h2


def normal_h1(size=10000):
    """A simple 1D histogram with normal distribution."""
    data = np.random.normal(0, 1, (size,))
    return h1(data)


def normal_h2(size=10000):
    """A simple 2D histogram with normal distribution."""
    data1 = np.random.normal(0, 1, (size,))
    data2 = np.random.normal(0, 1, (size,))
    return h2(data1, data2)


def munros(edge_length=10):
    """Number of munros in different rectangular areas of Scotland."""
    data = load_dataset("munros")
    return h2(data["lat"], data["long"], "fixed_width", edge_length / 60)


def load_dataset(name):
    """Load example dataset.
    
    If seaborn is present, its datasets can be loaded.
    """
    try:
        import seaborn.apionly as sns
        if name in sns.get_dataset_names():
            return sns.load_dataset(name)
    except ImportError:
        pass

    # Our custom datesets:
    if name == "munros":
        try:
            import pandas as pd
        except ImportError:
            raise RuntimeError("Pandas not installed.")
        import os
        path = os.path.join(os.path.dirname(__file__), "munros.csv")
        return pd.read_csv(path)

    # Fall through
    raise RuntimeError("Dataset {0} not available.".format(name))

ALL_EXAMPLES = [normal_h1, normal_h2]

try:
    import seaborn.apionly as sns

    def iris_h1(x="sepal_length"):
        iris = load_dataset("iris")
        return h1(iris[x], "human", 20, name="iris")


    def iris_h2(x="sepal_length", y="sepal_width"):
        iris = load_dataset("iris")
        return h2(iris[x], iris[y], "human", 20, name="iris")

    ALL_EXAMPLES += [iris_h1, iris_h2]
    
except ImportError:
    pass


