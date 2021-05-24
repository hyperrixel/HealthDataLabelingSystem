"""
HealthData Labeling System
==========================

module: HDLSSerializable
"""


from abc import abstractmethod


class HDLSSerializable:
    """
    Interface for HealthData Labeling System core objects
    =====================================================
    """

    __ATTRIBUTES = []


    @abstractmethod
    def __init__(self, initial_values : list = [], **kwargs):
        """
        Initialize the object
        =====================

        Parameters
        ----------
        initial_values : list, optional (empty list if omitted)
            List of tuple(str, str) elements to set initial values where element
            0 is the key and element 1 is the value.
        keyword arguments : str
            Arguments to set initial values.

        Raises
        ------
        AssertionError
            When both initial_values and keyword arguments are set.
        KeyError
            When a non existing key is given in initial_values.
        KeyError
            When a non existing key is given as keyword of a keyword argument.
        TypeError
            When element of initial_values is other than tuple.
        ValueError
            When a tuple in the initial_values has other length than 2.

        Notes
        -----
        I.
            Initial values and keyword arguments cannot be added at the same
            time.
        II.
            Both initial_values or keyword arguments have to contain valid
            arguments only. Valid keys are listed in __ATTRIBUTES.
        """


    @abstractmethod
    def from_json(self, json_string : str, **kwargs) -> any:
        """
        Abstract methot to build object from JSON string
        ================================================

        Parameters
        ----------
        json_string : str
            The JSON formatted string that contains all the needed data.
        keyword arguments
            Arguments to forward to json.loads() funtion.

        Returns
        -------
        any
            The object that is created.

        Notes
        -----
            This function requires a JSON string that is created with the
            .to_json() function of the same object type.
        """


    @abstractmethod
    def to_json(self, **kwargs) -> str:
        """
        Create JSON from an instance
        ============================

        Parameters
        ----------
        keyword arguments
            Arguments to forward to json.dunps() funtion.

        Returns
        -------
        str
            JSON formatted string.

        """
