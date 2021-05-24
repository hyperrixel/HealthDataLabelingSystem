"""
HealthData Labeling System
==========================

module: RawCollector
"""


from abc import abstractmethod
from os.path import isfile

from raw_collector import RawCollector
from raw_data import RawData


class RawStorage:
    """
    Provide raw data storage functions
    ==================================
    """


    @abstractmethod
    def __init__(self, json_str : str):
        """
        Intialize the object
        ====================

        Parameters
        ----------
        json_str : str
            JSON string to load configuration
        """


    @abstractmethod
    def create_storage(self, storage_name : str, permissions_json : str,
                       properties_json : str) -> str:
        """
        Create storage unit
        ===================

        Parameters
        ----------
        storage_name : str
            Name of the storage.
        permissions_json : str
            Permissions of the storage in the form of JSON string.
        properties_json : str
            Other properties of the storage in the form of JSON string.

        Returns
        -------
        str
            Storage ID if the storage is created, empty string if not.
        """


    @abstractmethod
    def create_user(self, user_name : str, permissions_json : str,
                    properties_json : str) -> str:
        """
        Create user
        ===========

        Parameters
        ----------
        user_name : str
            Name of the user.
        permissions_json : str
            Permissions of the user in the form of JSON string.
        properties_json : str
            Other properties of the user in the form of JSON string.

        Returns
        -------
        str
            User ID if the user is created, empty string if not.
        """


    @abstractmethod
    def delete(self, staorage_id : str, data_entry_id : str) -> bool:
        """
        Delete data entry
        =================

        Parameters
        ----------
        staorage_id : str
            ID of the storage to delete from.
        data_entry_id : str
            ID of the data entry to delete.

        Returns
        -------
        bool
            True if deletion was successful, False if not.
        """


    @abstractmethod
    def delete_storage(self, staorage_id : str) -> bool:
        """
        Delete storage unit
        ===================

        Parameters
        ----------
        staorage_id : str
            ID of the storage to delete.

        Returns
        -------
        bool
            True if deletion was successful, False if not.
        """


    @abstractmethod
    def delete_user(self, user_id : str) -> bool:
        """
        Delete user
        ===========

        Parameters
        ----------
        user_id : str
            ID of the user to delete.

        Returns
        -------
        bool
            True if deletion was successful, False if not.
        """


    @abstractmethod
    def from_file(cls, json_path : str, encoding : str = "utf8") -> any:
        """
        Load instance from JSON file
        ============================

        Parameters
        ----------
        json_path
            Path to an existing JSON file.
        encoding : str, optional ("utf8" if omitted)
            Encoding to use while loading the file.

        Returns
        -------
        amy (subclass of RawStorage)
            The new RawStorage object.
        """


    @abstractmethod
    def get(self, staorage_id : str, data_entry_id : str) -> RawData:
        """
        Delete data entry
        =================

        Parameters
        ----------
        staorage_id : str
            ID of the storage to get from.
        data_entry_id : str
            ID of the data entry to get.

        Returns
        -------
        RawData
            The data.
        """


    @abstractmethod
    def get_storage(self, staorage_id : str) -> tuple:
        """
        Get storage unit information
        ============================

        Parameters
        ----------
        staorage_id : str
            ID of the storage to get.

        Returns
        -------
        tuple(str, str, st)
            Storage data in the form of a tuple, where element 0 is the name
            of the storage unit, element 1 is a JSON string with the storage
            unit level permissions and element 2 is a JSON string with the
            storage unit level properties.
        """


    @abstractmethod
    def get_user(self, user_id) -> tuple:
        """
        Get user information
        ====================

        Parameters
        ----------
        user_id : str
            ID of the user to get.

        Returns
        -------
        tuple(str, str, st)
            User data in the form of a tuple, where element 0 is the user's
            name, element 1 is a JSON string with the user's permissions and
            element 2 is a JSON string with the user's properties.
        """


    @abstractmethod
    def insert(self, staorage_id : str, data : RawData) -> str:
        """
        Insert a new data entry in the storage
        ======================================

        Parameters
        ----------
        staorage_id : str
            ID of the storage to insert.
        data : RawData
            Data to insert

        Returns
        -------
        str
            ID of the data entry.
        """


    @abstractmethod
    def login(self, user_id : str, user_name : str, token : str) -> bool:
        """
        Log a user in
        =============

        Parameters
        ----------
        user_id : str
            ID of the user to log in. If empty, name should be non-empty.
        user_name : str
            Name of the user to log in. If empty, ID should be non-empty.
        token : str
            Token to use. Token can be password or real token in enconded or
            not encoded form.

        Returns
        -------
        bool
            True if login was successful, False if not.

        Notes
        -----
        I.
            This function should raise ValueError if both user_id and user_name
            are empty.
        II.
            Oni one user can be logged in at once with the same RawStorage
            instance.
        """


    @abstractmethod
    def logout(self) -> bool:
        """
        Log out user
        ============

        Returns
        -------
        bool
            True if logging out was successful, False if not.
        """


    def update(self, staorage_id : str, data_entry_id : str, data : RawData):
        """
        Delete data entry
        =================

        Parameters
        ----------
        staorage_id : str
            ID of the storage to delete from.
        data_entry_id : str
            ID of the data entry to delete.
        data : RawData
            Data to apply on update.

        Raises
        ------
        PermissionError
            If this function is called because updateing a stored raw data is
            not allowed due to it is a bad practice.
        """

        raise PermissionError('RawStorage.update(): update of stored raw data' +
                              ' is not allowed.')


    @abstractmethod
    def update_storage(self, staorage_id : str, storage_name : str,
                     permissions_json : str, properties_json : str) -> bool:
        """
        Update storage unit
        ===================

        Parameters
        ----------
        staorage_id : str
            ID of the storage to update.
        storage_name : str
            Name of the storage. If empty, the name of the storage will be
            unchanged.
        permissions_json : str
            Unit level permissions related to the storage unit in the form of
            JSON string. If empty, no permiision is changed.
        properties_json : str
            Other properties of the storage unit in the form of JSON string.
            if empty, no property is changed.

        Returns
        -------
        bool
            True if the update was successful, False if not.
        """


    @abstractmethod
    def update_user(self, user_id : str, user_name : str,
                     permissions_json : str, properties_json : str) -> bool:
        """
        Update user
        ===========

        Parameters
        ----------
        user_id : str
            ID of the user to update.
        user_name : str
            Name of the user. If empty, user's name will be unchanged.
        permissions_json : str
            Permissions of the user in the form of JSON string. If empty, no
            permiision is changed.
        properties_json : str
            Other properties of the user in the form of JSON string. if empty,
            no property is changed.

        Returns
        -------
        bool
            True if the update was successful, False if not.
        """
