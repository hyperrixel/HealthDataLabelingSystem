"""
HealthData Labelig System
==========================

module: RawData
"""


from time import time


class RawData:
    """
    Provide raw data structure
    ==========================

    Attributes
    ----------
    data : str (read-only)
        The stored ata
    device_id : str (read-only)
        The stored device ID
    source_id : str (read-only)
        The ID of the source in the device
    time_section : int (read-only)

    timestamp : int (read-only)
        Second precision timestamp
    """


    def __init__(self, device_id : str, source_id : str, data : str,
                 timestamp : int = 0, time_section : int = 0):
        """
        Intialize the object
        ====================

        Parameters
        ----------
        device_id : str
            ID of the device where the data comes from.
        source_id : str
            ID of the actual source in the device where the data comes from.
        data : str
            The stored data.
        timestamp : int, optional (0 if omitted)
            Timestap in form of seconds. If 0 is gien, the current timestamp is
            stored.
        time_section int, optional (0 if omitted)
            Section of the second. It can be used to store milliseconds or any
            other measure that is smaller then the second.
        """

        self.__device_id = device_id
        self.__source_id = source_id
        self.__data = data
        if timestamp == 0:
            self.__timestamp = int(time)
        else:
            self.__timestamp = timestamp
        self.__time_section = time_section


    @property
    def data(self) -> str:
        """
        Get data

        Returns
        -------
        str
            The stored data.
        """

        return self.__data


    @property
    def device_id(self) -> str:
        """
        Get device ID
        =============

        Returns
        -------
        str
            The stored davice ID.
        """

        return self.__device_id


    @property
    def source_id(self) -> str:
        """
        Get source ID
        =============

        Returns
        -------
        str
            The stored source ID in the device.
        """

        return self.__source_id


    @property
    def time_section(self) -> int:
        """
        Get time section
        ================

        Returns
        -------
        str
            The stored section of time.
        """

        return self.__time_section


    @property
    def timestamp(self) -> int:
        """
        Get timestamp
        =============

        Returns
        -------
        str
            The stored second precision timestamp.
        """

        return self.__timestamp


    def __repr__(self) -> str:
        """
        Get programmer friendly string representation of the object
        ===========================================================
        """

        result = 'Rawdata(device_id={}, source_id={}, data={}, '.format(
                  self.device_id, self.source_id, self.data)
        result += 'timestamp={}, time_section={})'.format(
                   self.timestamp, self.time_section)
        return result


    def __str__(self) -> str:
        """
        Get string representation of the object
        =======================================
        """

        result = 'Rawdata: timestamp: {}; time_section: {};'.format(
                  self.timestamp, self.time_section)
        result += ' device_id: {}; source_id: {}; data: {}'.format(
                   self.device_id, self.source_id, self.data)
        return result
