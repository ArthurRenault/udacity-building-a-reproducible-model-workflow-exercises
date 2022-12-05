import numpy as np
import pandas as pd


def test_dummy():
    assert True


def test_import_success():
    import pandas
    import numpy

    pandas.DataFrame()
    numpy.array([])

    assert True


def test_import_fail():
    import scipy

    print(scipy.stats)

    assert True
