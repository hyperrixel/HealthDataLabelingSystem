"""
HealthData Labeling System
==========================

module: Origins
"""


from enum import Enum


class Origins(Enum):
    """
    Provide constants to describe data point's origin
    =================================================

    Notes
    -----
        The meanings of Origins constants:
            RAW : data object contains raw data
            RAW_LABELED : data object contains labaled raw data
    """

    RAW = 'raw'
    RAW_LABELED = 'raw_labeled'
