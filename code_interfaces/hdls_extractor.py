class HDLSDataObject:
    """
    Represent a datapoint
    =====================
    """

    def __init__(self, value : str, unit : str, attributes : dict):
        """
        Initialize the object
        =====================

        Parameters
        ----------
        value : str
            Value to store.
        unit : str
            Unit to store.
        attributes : dict
            Attributes of the datapoint in form of { string : string}.
        """


    @property
    def attributes(self) -> dict:
        """
        Get all attributes of the object
        ================================

        Returns
        -------
        dict
            Copy of the attributes.
        """

        return self.__attributes[:]


    @staticmethod
    def from_json(json_string : str) -> HDLSDataObject:
        """
        Generate object from JSON string
        ================================

        Parameters
        ----------
        json_string : str
            JSON string represenatiton of a HDLSDataObject.

        Returns
        -------
        HDLSDataObject
            The restored object.
        """


    def get(self, key : str) -> str:
        """
        Get an attribute by key
        =======================

        Parameters
        ----------
        key : str
            Key to get.

        Returns
        -------
        str
            Value of the key.

        Notes
        -----
        Depending on the behavior set by the use case, this function rases
        error, warning or returns an empty string if key doesn't exist.
        """


    def has(self, key : str) -> bool:
        """
        Check wether a key exist
        ========================

        Parameters
        ----------
        key : str
            Key to check.

        Returns
        -------
        bool
            True if the key exists, False if not.
        """


    def is_true(self, key : str) -> bool:
        """
        Check wether a key is set to True
        =================================

        Parameters
        ----------
        key : str
            Key to check.

        Returns
        -------
        bool
            True if the key is TRUE, False if not.
        """


    def time(self) -> float:
        """
        Get timestamp of the object
        ===========================

        Returns
        -------
        float
            Timestamp in milliseconds.
        """


    def to_json(self) -> str:
        """
        Convert object to JSON string
        =============================

        Returns
        -------
        str
            JSON represenation of the object.
        """


    @property
    def unit(self) -> str:
        """
        Get the measurement unit
        ========================

        Returns
        -------
        str
            The measurement unit of the object.
        """

        return self.__unit


    @property
    def value(self) -> str:
        """
        Get the value
        =============

        Returns
        -------
        str
            The value of the object.
        """

        return self.__value


class HDLSExtractor:
    """
    Extract data from source
    ========================
    """

    def __init__(self, use_case_id : str):
        """
        Initialize the object
        =====================

        Parameters
        ----------
        use_case_id : str
            The use case ID to initialize to.

        Notes
        -----
            Depending on the behavior set by the use case, this function rases
            error, warning or doesn't create the object on error.
        """


    def delete_data(self, conditions : str) -> bool:
        """
        Delete data
        ===========

        Parameters
        ----------
        conditions : str
            Query string of conditions.

        Returns
        -------
        bool
            True if deletion was successful, False if not.

        Notes
        -----
            Depending on the behavior set by the use case, this function rases
            error, warning or simply returns False on error.
        """


    def get(self, source_id : str, data_profile_id : str,
            store : bool = False) -> HDLSDataObject:
        """
        Get data
        ========

        Parameters
        ----------
        source_id : str
            ID of the source to use to get.
        data_profile_id : str
            ID of the data prifle to use by conversion.
        store : bool, optional (False if omitted)
            Whether to store the data or not.

        Notes
        -----
            Depending on the behavior set by the use case, this function rases
            error, warning or simply returns empty HDLSDataObject on error.
        """

    def match(self, current_use_case_id : str) -> bool:
        """
        Check whether use case matches
        ==============================

        Parameters
        ----------
        current_use_case_id : str
            Use case ID to check.

        Returns
        -------
        bool
            True if the use case ID matches, False if not.
        """

        return self.__use_case_id == current_use_case_id


class HDLSIntegrator:
    """
    Integrate data to source
    ========================
    """

    def __init__(self, use_case_id : str):
        """
        Initialize the object
        =====================

        Parameters
        ----------
        use_case_id : str
            The use case ID to initialize to.

        Notes
        -----
            Depending on the behavior set by the use case, this function rases
            error, warning or doesn't create the object on error.
        """

    def delete_data(self, condition_str : str) -> bool:
        """
        Delete data
        ===========

        Parameters
        ----------
        conditions : str
            Query string of conditions.

        Returns
        -------
        bool
            True if deletion was successful, False if not.

        Notes
        -----
            Depending on the behavior set by the use case, this function rases
            error, warning or simply returns False on error.
        """


    def match(self, current_use_case_id : str) -> bool:
        """
        Check whether use case matches
        ==============================

        Parameters
        ----------
        current_use_case_id : str
            Use case ID to check.

        Returns
        -------
        bool
            True if the use case ID matches, False if not.
        """

        return self.__use_case_id == current_use_case_id


    def send(self, destination_id : str, output_data_profile_id : str,
             data : HDLSDataObject, store : bool = False):
        """
        Send data to destination
        ========================

        Parameters
        ----------
        destination_id : str
            ID of the destination to send to.
        output_data_profile_id : str
            ID of the output data profile to use.
        data : HDLSDataObject
            Data to send.
        store : bool, optional (False, if omitted)
            Whether to store the data or not.

        Notes
        -----
            Depending on the behavior set by the use case, this function rases
            error, warning or simply ends on error.
        """
