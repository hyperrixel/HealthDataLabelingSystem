"""
HealthData Labeling System
==========================

module: HDLSDataObject
"""


from enum_origins import Origins
from enum_measures import Measures
from hdls_label_object import HDLSLabelObject


class HDLSDataObject:
    """
    Provide base data object for HealthData Labeling System
    =======================================================

    Attributes
    ----------
    is_complete : bool (read-only)
        Whether each attribute is set or not.
    labels : list (read-only)
        List of labels.
    measure : str
        The measure unit of the data in the data point.
    name : str
        The name of the data point.
    origin : str
        The origin of the data in the data point.
    value : str
        The actual value of the data point.
    """


    __ATTRIBUTES = ['labels', 'measure', 'name', 'origin', 'value']


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

        self.__labels = {}
        self.__measure = ''
        self.__name = ''
        self.__origin = ''
        self.__value = ''
        if len(initial_values) > 0:
            if len(kwargs) > 0:
                raise AssertionError('HDLSDataObject.init(): initial_values' +
                                     'and keyword argomuents cannot be set at' +
                                     ' the same time.')
            else:
                for element in initial_values:
                    if isinstance(element, tuple):
                        if len(element) == 2:
                            if element[0] in self.__ATTRIBUTES:
                                if element[0] != 'labels':
                                    setattr(self, element[0], element[1])
                                else:
                                    self.add_labels(element[1])
                            else:
                                raise KeyError('HDLSDataObject.init(): ' +
                                               'invalid attribute name to set.')
                        else:
                            raise ValueError('HDLSDataObject.init(): tuples ' +
                                             'of initial_values must contain ' +
                                             'exactly 2 elements')
                    else:
                        raise TypeError('HDLSDataObject.init(): elements of ' +
                                        'initial_values must be tuple.')
        else:
            for key, value in kwargs.items():
                if key not in self.__ATTRIBUTES:
                    raise KeyError('HDLSDataObject.init(): keyword for' +
                                   'attribute name to set is invalid.')
                if key != 'labels':
                    setattr(self, key, value)
                else:
                    self.add_labels(value)


    def add_label(self, label_data : any = [], **kwargs) -> int:
        """
        Add label to the data point
        ===========================

        Parameters
        ----------
        label_data : HDLSLabelObject | list(tuple(str, str))
            Label to add, or list of tuples to create a label to add.
        keyword arguments : str
            Arguments to create a label to add.

        Returns
        -------
        int
            The ID of the label.

        Raises
        ------
        AssertionError
            When both label_data and keyword arguments are set.
        AssertionError
            When label_data is an empty list or is not given and no keyword
            argument is given at the same time.
        TypeError
            When label_data is given but is other type than HDLSLabelObject or
            list.

        Notes
        -----
            Labal data and keyword arguments cannot be added at the same time.
        """

        if isinstance(label_data, HDLSLabelObject):
            if len(kwargs) > 0:
                raise AssertionError('HDLSDataObject.add_label(): label_data ' +
                                     'and keyword argomuents cannot be set at' +
                                     ' the same time.')
            _label = label_data
        elif isinstance(label_data, list):
            if len(label_data) > 0:
                if len(kwargs) > 0:
                    raise AssertionError('HDLSDataObject.add_label(): ' +
                                         'label_data and keyword argomuents ' +
                                         'cannot be set at the same time.')
                _label = HDLSLabelObject(label_data)
            else:
                if len(kwargs) > 0:
                    _label = HDLSLabelObject(**kwargs)
                else:
                    raise AssertionError('HDLSDataObject.add_label(): neither' +
                                         'label_data nor keyword arguments ' +
                                         'were given to create HDLSDataObject.')
        else:
            raise TypeError('HDLSDataObject.add_label(): type of label_data ' +
                            'must be HDLSDataObject or list of tuples.')
        if not _label.is_complete:
            raise ValueError('HDLSDataObject.add_label(): added label must ' +
                             'complete.')
        _id = len(self.__labels)
        self.__labels[_id] = _label
        return _id


    def add_labels(self, labels : list) -> list:
        """
        Add multiple labels to the data point
        =====================================

        Parameters
        ----------
        labels : list
            Labels or label informations to add.

        Returns
        -------
        list[int]
            List of the IDs.
        """

        result = []
        for label in labels:
            if isinstance(label, (HDLSDataObject, list)):
                result.append(self.add_label(label))
            elif isinstance(label, dict):
                result.append(self.add_label(**label))
            else:
                raise TypeError('HDLSDataObject.add_labels(): elements in ' +
                                'labels must be instances of HDLSLabelObject,' +
                                ' list or dict.')
        return result


    def delete_label(self, id_to_delete : int):
        """
        Delete label from the data point
        ================================

        Parameters
        ----------
        id_to_delete : int
            The id of the label to delete.

        Raises
        ------
        ValueError
            When tried to delete an element that have been deleted.
        IndexError
            When tried to delete a non-existing id.
        """

        if id_to_delete in self.__labels.keys():
            if self.__labels[id_to_delete] is not None:
                self.__labels[id_to_delete] = None
            else:
                raise ValueError('HDLSDataObject.delete_label(): tried to ' +
                               'delete an element id that is already deleted.')
        else:
            raise IndexError('HDLSDataObject.delete_label(): tried to delete ' +
                           'a non-existing id.')


    def get_label_by_id(self, id_to_get : int) -> HDLSLabelObject:
        """
        Get a label by id
        =================

        Parameters
        ----------
        id_to_get : int
            Id for getting a specified label from the data point.

        Returns
        -------
        HDLSLabelObject
            The label itself.

        Raises
        ------
        IndexError
            When tried to get an element that is never existed.
        ValueError
            When tried to get an element that have been deleted.
        """

        if id_to_get not in self.__labels.keys():
            raise IndexError('HDLSDataObject.get_label_by_id(): tried to get ' +
                             'a label by id, that never existed.')
        if self.__labels[id_to_get] is None:
            raise ValueError('HDLSDataObject.get_label_by_id(): tried to get ' +
                           'a deleted element by id.')
        return self.__labels[id_to_get]


    @property
    def is_complete(self) -> bool:
        """
        Get wheter the data point is complete or not
        ============================================

        Returns
        -------
        bool
            True if the label is complete, False if not.
        """

        return all([self.labels_count > 0, self.measure != '', self.name != '',
                    self.origin != '', self.value != ''])


    @property
    def labels(self) -> dict:
        """
        Get labels of the data point
        ============================

        Returns
        -------
        dict
            Copy of the dict of the labels.
        """

        result = {}
        for key, value in self.__labels.items():
            if value is not None:
                result[key] = value
        return result


    @property
    def labels_count(self) -> int:
        """
        Get count of labels of the data point
        =====================================

        Returns
        -------
        int
            Count of non-deleted labels.
        """

        result = 0
        for value in self.__labels.values():
            if value is not None:
                result += 1
        return result


    @property
    def measure(self) -> str:
        """
        Get the measure of the data point
        =================================

        Returns:
        str
            The measure as string.
        """

        return self.__measure


    @measure.setter
    def measure(self, new_value : any):
        """
        Set the measure of the data point
        =================================

        Parameters
        ----------
        new_value : Measures | str
            The measure to set.

        Raises
        ------
        TypeError
            When the new value is nor Measures nor string.
        ValueError
            When the new value is not a value from the Measures enum.
        """

        if isinstance(new_value, Measures):
            self.__measure = new_value.value
        elif isinstance(new_value, str):
            if new_value in [element.value for element in Measures]:
                self.__measure = new_value
            else:
                raise ValueError('HDLSDataObject.measure: tried to set an ' +
                                 'invalid origin.')
        else:
            raise TypeError('HDLSDataObject.measure: new value must be type ' +
                            'of Measures or string.')


    @property
    def name(self) -> str:
        """
        Get the name of the data point
        ==============================

        Returns
        -------
        str
            The name of the data point.
        """

        return self.__name


    @name.setter
    def name(self, new_value : str):
        """
        Get the name of the data point
        ==============================

        Parameters
        ----------
        new_value : str
            Name of the data point to set.
        """

        self.__name = new_value


    @property
    def origin(self) -> str:
        """
        Get the origin of the data point
        ================================

        Returns:
        str
            The origin as string.
        """

        return self.__origin


    @origin.setter
    def origin(self, new_value : any):
        """
        Set the origin of the data point
        ================================

        Parameters
        ----------
        new_value : Origins | str
            The origin to set.

        Raises
        ------
        TypeError
            When the new value is nor Origins nor string.
        ValueError
            When the new value is not a value from the Origins enum.
        """

        if isinstance(new_value, Origins):
            self.__origin = new_value.value
        elif isinstance(new_value, str):
            if new_value in [element.value for element in Origins]:
                self.__origin = new_value
            else:
                raise ValueError('HDLSDataObject.origin: tried to set an ' +
                                 'invalid origin.')
        else:
            raise TypeError('HDLSDataObject.origin: new value must be type of' +
                            ' Origins or string.')


    def update_label(self, id_to_update : int, label_data : any = [], **kwargs):
        """
        Add label to the data point
        ===========================

        Parameters
        ----------
        id_to_update : int
            ID to update.
        label_data : HDLSLabelObject | list(tuple(str, str))
            Label to add, or list of tuples to create a label to add.
        keyword arguments : str
            Arguments to create a label to add.

        Returns
        -------
        int
            The ID of the label.

        Raises
        ------
        AssertionError
            When both label_data and keyword arguments are set.
        AssertionError
            When label_data is an empty list or is not given and no keyword
            argument is given at the same time.
        TypeError
            When label_data is given but is other type than HDLSLabelObject or
            list.

        Raises
        ------
        IndexError
            When tried to get an element that is never existed.

        Notes
        -----
            Labal data and keyword arguments cannot be added at the same time.
        """

        if id_to_update not in self.__labels.keys():
            raise IndexError('HDLSDataObject.update_label(): tried to update ' +
                             'a label by id, that never existed.')
        if isinstance(label_data, HDLSLabelObject):
            if len(kwargs) > 0:
                raise AssertionError('HDLSDataObject.update_label(): ' +
                                     'label_data and keyword argomuents ' +
                                     'cannot be set at the same time.')
            _label = label_data
        elif isinstance(label_data, list):
            if len(label_data) > 0:
                if len(kwargs) > 0:
                    raise AssertionError('HDLSDataObject.update_label(): ' +
                                         'label_data and keyword argomuents ' +
                                         'cannot be set at the same time.')
                _label = HDLSLabelObject(label_data)
            else:
                if len(kwargs) > 0:
                    _label = HDLSLabelObject(**kwargs)
                else:
                    raise AssertionError('HDLSDataObject.update_label(): ' +
                                         'neither label_data nor keyword ' +
                                         'arguments were given to create ' +
                                         'HDLSDataObject.')
        else:
            raise TypeError('HDLSDataObject.update_label(): type of ' +
                            'label_data must be HDLSDataObject or list of ' +
                            'tuples.')
        if not _label.is_complete:
            raise ValueError('HDLSDataObject.update_label(): added label must' +
                             'complete.')
        self.__labels[id_to_update] = _label


    @property
    def value(self) -> str:
        """
        Get the value of the data point
        ===============================

        Returns:
        str
            The value itself.
        """

        return self.__value


    @value.setter
    def value(self, new_value : str):
        """
        Set the value of the data point
        ===============================

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

        result = 'HDLSDataObject: name: {}; origin: {}; measure: {};'.format(
                  self.name, self.origin, self.measure)
        result += ' value: {}\n--- has {} labels and {}.'.format(self.value,
                   self.labels_count, 'is complete' if self.is_complete else
                   'is not complete')
        result += '\n--- Labels:\n'
        for key, value in self.__labels.items():
            result += '--- --- {}: {}\n'.format(key, value)
        return result
