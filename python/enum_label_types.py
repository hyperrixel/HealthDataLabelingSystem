"""
HealthData Labeling System
==========================

module: LabelTypes
"""


from enum import Enum


class LabelTypes(Enum):
    """
    Provide constants to describe data label types
    ==============================================

    Notes
    -----
        The meanings of LabelTypes constants:
            CONTEXT : label to describe context.
            DATA : label to describe data information.
            LEGAL : label to describe legal information.
            LIFECYCLE : label to describe information about the life cycle.
            PERMISSION : label to describe information about permissions.
            OWNERSHIP : label to describe information about the ownership.
            USER : label to describe information about realted users.
            TAXONOMY : label to describe taxonomy information.
            TIME : label to describe time.
    """

    CONTEXT = 'context'
    DATA = 'data'
    LEGAL = 'legal'
    LIFECYCLE = 'lifecycle'
    PERMISSION = 'permission'
    OWNERSHIP = 'ownership'
    USER = 'user'
    TAXONOMY = 'taxonomy'
    TIME = 'time'
