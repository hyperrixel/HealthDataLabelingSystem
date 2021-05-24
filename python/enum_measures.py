"""
HealthData Labeling System
==========================

module: Measures
"""


from enum import Enum


class Measures(Enum):
    """
    Provide constants to describe data point's measure
    ==================================================

    Notes
    -----
        The meanings of Measures constants:
            DATA : the value of the data point is rather data alike than
                   anything else.
            METER : the value of the data object is in meters.
    """

    DATA = 'data'
    METER = 'meter'
