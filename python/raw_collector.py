"""
HealthData Labeling System
==========================

module: RawCollector
"""


from abc import abstractmethod

from raw_data import RawData


class RawCollector:
    """
    Provide raw data collector functions
    ====================================
    """


    def __init__(self):
        """
        Intialize the object
        ====================
        """

        self._content = []
        self.__start_id = 0
        self.__new_from = 0


    def clean(self):
        """
        Clean content
        =============
        """

        self.content = []


    @abstractmethod
    def collect(self, device_id : any, source_id : any, data : any,
                timestamp : int = 0, time_section : int = 0):
        """
        Collect data from device

        Parameters
        ----------
        device_id : any
            Device ID of the signaling device.
        source_id : any
            Source ID of the signal. (Source ID relaitve to the device.)
        data : any
            Data of the signal.
        timestamp : int, optional (0 if omitted)
            Timestamp of the registration of the signal. If 0 is given, the
            signal gets registered to the call of the function. Timestamp is
            second precision value.
        time_section int, optional (0 if omitted)
            Time section of the signal. This value can be used to add
            millisencond precision to timestamp or to mark various series of
            data at the same time.

        Notes
        -----
        I.
            Expected worklof of this functiun is to convert parameters into
            RawData object and add RawData object to the end of the container
            self._content.
        II.
            To fit the requirements of HealthData Labeling System device_id,
            source_id and data parameters should be converted to string.
        III.
            Tha final content of data must be a JSON compatible string to
            provide flexible usability. In most cases this means the use of
            dumps() function from the json standard library but unique solutions
            also can be reasonable.
        """


    def flush(self) -> list:
        """
        Flush new data
        ==============

        Returns
        -------
        list[RawData]
            List of RawData objects.
        """

        result = self._content[self.__new_from:]
        self.__new_from = len(self._content)
        return result


    def get(self, from_id : int = 0, to_id : int = 0) -> list:
        """
        Get range of data
        =================

        Parameters
        ----------
        from_id : int
            Beginning of the range (inclusive).
        to_id : int
            End of the range (non-inclusive).

        Returns
        -------
        list[RawData]
            List of RawData objects.

        Raises
        ------
        IndexError
            If from_id is index that doesn't exist in the content.
        IndexError
            If to_id is index that doesn't exist in the content.
        """

        if from_id >= len(self._content):
            raise IndexError('RawCollector.get(): from_id out of range.')
        if to_id > len(self._content):
            raise IndexError('RawCollector.get(): to_id out of range.')
        return self._content[from_id:to_id]


    def get_by_id(self, data_id : int) -> RawData:
        """
        Get data by ID
        ==============

        Parameters
        ----------
        data_id : int
            ID of the data to get.

        Returns
        -------
        RawData
            The data.

        Raises
        ------
        IndexError
            If data_id is index that doesn't exist in the content.
        """

        if data_id < -len(self._content) or data_id >= len(self._content):
            raise IndexError('RawCollector.get_by_id(): data_id out of range.')
        return self._content[data_id]


    def has_new(self) -> bool:
        """
        Get whether are there new data elements or not
        ==============================================
        """

        return len(self._content) >= self.__new_from - self.__start_id


    def __len__(self) -> int:
        """
        Get length of stored data
        =========================
        """

        return len(self._content)
