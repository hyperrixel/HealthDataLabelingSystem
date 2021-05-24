"""
HealthData Labeling System
==========================

module: HDLSLabelObject
"""


from enum_label_types import LabelTypes


class HDLSLabelObject:
    """
    Provide base label object for HealthData Labeling System
    ========================================================

    Attributes
    ----------
    is_complete : bool (read-only)
        Whether each attribute is set or not.
    name : str
        Tha name of the label.
    type : str
        The type of the label.
    value : str
        The value of the label.
    """


    __ATTRIBUTES = ['name', 'type', 'value']


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

        self.__name = ''
        self.__type = ''
        self.__value = ''
        if len(initial_values) > 0:
            if len(kwargs) > 0:
                raise AssertionError('HDLSLabelObject.init(): initial_values' +
                                     'and keyword argomuents cannot be set at' +
                                     ' the same time.')
            else:
                for element in initial_values:
                    if isinstance(element, tuple):
                        if len(element) == 2:
                            if element[0] in self.__ATTRIBUTES:
                                setattr(self, element[0], element[1])
                            else:
                                raise KeyError('HDLSLabelObject.init(): ' +
                                               'invalid attribute name to set.')
                        else:
                            raise ValueError('HDLSLabelObject.init(): tuples ' +
                                             'of initial_values must contain ' +
                                             'exactly 2 elements')
                    else:
                        raise TypeError('HDLSLabelObject.init(): elements of ' +
                                        'initial_values must be tuple.')

        else:
            if len(kwargs) > 0:
                for key, value in kwargs.items():
                    if key in self.__ATTRIBUTES:
                        setattr(self, key, value)
                    else:
                        raise KeyError('HDLSLabelObject.init(): invalid ' +
                                       'attribute name to set.')


    @property
    def is_complete(self) -> bool:
        """
        Get wheter the label is complete or not
        =======================================

        Returns
        -------
        bool
            True if the label is complete, False if not.
        """

        return all([self.name != '', self.type != '', self.value != ''])


    @property
    def name(self) -> str:
        """
        Get label name
        ==============

        Returns
        -------
        str
            The name of the label.
        """

        return self.__name


    @name.setter
    def name(self, new_value : str):
        """
        Set label name
        ==============

        Parameters
        ----------
        new_value : str
            Name of the label to set.
        """

        self.__name = new_value


    @property
    def type(self) -> str:
        """
        Get label type
        ==============

        Returns
        -------
        str
            The type of the label.
        """

        return self.__type


    @type.setter
    def type(self, new_value : any):
        """
        Set label type
        ==============

        Parameters
        ----------
        new_value : LabelTypes | tr
            Type of the label to set.

        Raises
        ------
        TypeError
            When the new value is nor LabelTypes nor string.
        ValueError
            When the new value is not a value from the LabelTypes enum.
        """

        if isinstance(new_value, LabelTypes):
            self.__type = new_value.value
        elif isinstance(new_value, str):
            if new_value in [element.value for element in LabelTypes]:
                self.__type = new_value
            else:
                raise ValueError('HDLSLabelObject.type: tried to set an ' +
                                 'invalid type.')
        else:
            raise TypeError('HDLSLabelObject.type: new value must be type of' +
                            ' LabelTypes or string.')


    @property
    def value(self) -> str:
        """
        Get label value
        ===============

        Returns:
        str
            The value itself.
        """

        return self.__value


    @value.setter
    def value(self, new_value : str):
        """
        Set label value
        ===============

        Parameters
        ----------
        new_value : str
            The valu to set.
        """

        self.__value = new_value


    def __str__(self) -> str:
        """
        Get string representation of the object
        =======================================
        """

        result = 'hdls_label_object: name {}; type: {}; value {}'.format(
                 self.name, self.type, self.value)
        return result    
