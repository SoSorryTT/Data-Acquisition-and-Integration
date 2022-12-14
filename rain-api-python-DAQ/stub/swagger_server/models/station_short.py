# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class StationShort(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, station_id: int=None, name: str=None):  # noqa: E501
        """StationShort - a model defined in Swagger

        :param station_id: The station_id of this StationShort.  # noqa: E501
        :type station_id: int
        :param name: The name of this StationShort.  # noqa: E501
        :type name: str
        """
        self.swagger_types = {
            'station_id': int,
            'name': str
        }

        self.attribute_map = {
            'station_id': 'stationId',
            'name': 'name'
        }
        self._station_id = station_id
        self._name = name

    @classmethod
    def from_dict(cls, dikt) -> 'StationShort':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The StationShort of this StationShort.  # noqa: E501
        :rtype: StationShort
        """
        return util.deserialize_model(dikt, cls)

    @property
    def station_id(self) -> int:
        """Gets the station_id of this StationShort.


        :return: The station_id of this StationShort.
        :rtype: int
        """
        return self._station_id

    @station_id.setter
    def station_id(self, station_id: int):
        """Sets the station_id of this StationShort.


        :param station_id: The station_id of this StationShort.
        :type station_id: int
        """

        self._station_id = station_id

    @property
    def name(self) -> str:
        """Gets the name of this StationShort.


        :return: The name of this StationShort.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this StationShort.


        :param name: The name of this StationShort.
        :type name: str
        """

        self._name = name
