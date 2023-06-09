# -*- coding: utf-8 -*-
import numpy as np

from hbtpy.soicc import calculate_g2


def test_g2():
    """
    test that the g2 calculator is functioning correctly
    """
    i1 = np.ones([50, 50])
    i2 = i1
    assert np.array_equal(calculate_g2(i1, i2), i1) is True, "Correlation Calculator Failed"
