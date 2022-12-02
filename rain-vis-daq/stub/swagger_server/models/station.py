# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Station(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, station_id: int=None, basin_id: int=None, name: str=None, lat: float=None, lon: float=None):  # noqa: E501
        """Station - a model defined in Swagger

        :param station_id: The station_id of this Station.  # noqa: E501
        :type station_id: int
        :param basin_id: The basin_id of this Station.  # noqa: E501
        :type basin_id: int
        :param name: The name of this Station.  # noqa: E501
        :type name: str
        :param lat: The lat of this Station.  # noqa: E501
        :type lat: float
        :param lon: The lon of this Station.  # noqa: E501
        :type lon: float
        """
        self.swagger_types = {
            'station_id': int,
            'basin_id': int,
            'name': str,
            'lat': float,
            'lon': float
        }

        self.attribute_map = {
            'station_id': 'stationId',
            'basin_id': 'basinId',
            'name': 'name',
            'lat': 'lat',
            'lon': 'lon'
        }
        self._station_id = station_id
        self._basin_id = basin_id
        self._name = name
        self._lat = lat
        self._lon = lon

    @classmethod
    def from_dict(cls, dikt) -> 'Station':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Station of this Station.  # noqa: E501
        :rtype: Station
        """
        return util.deserialize_model(dikt, cls)

    @property
    def station_id(self) -> int:
        """Gets the station_id of this Station.


        :return: The station_id of this Station.
        :rtype: int
        """
        return self._station_id

    @station_id.setter
    def station_id(self, station_id: int):
        """Sets the station_id of this Station.


        :param station_id: The station_id of this Station.
        :type station_id: int
        """

        self._station_id = station_id

    @property
    def basin_id(self) -> int:
        """Gets the basin_id of this Station.


        :return: The basin_id of this Station.
        :rtype: int
        """
        return self._basin_id

    @basin_id.setter
    def basin_id(self, basin_id: int):
        """Sets the basin_id of this Station.


        :param basin_id: The basin_id of this Station.
        :type basin_id: int
        """

        self._basin_id = basin_id

    @property
    def name(self) -> str:
        """Gets the name of this Station.


        :return: The name of this Station.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Station.


        :param name: The name of this Station.
        :type name: str
        """

        self._name = name

    @property
    def lat(self) -> float:
        """Gets the lat of this Station.

        Latitude  # noqa: E501

        :return: The lat of this Station.
        :rtype: float
        """
        return self._lat

    @lat.setter
    def lat(self, lat: float):
        """Sets the lat of this Station.

        Latitude  # noqa: E501

        :param lat: The lat of this Station.
        :type lat: float
        """

        self._lat = lat

    @property
    def lon(self) -> float:
        """Gets the lon of this Station.

        Longitude  # noqa: E501

        :return: The lon of this Station.
        :rtype: float
        """
        return self._lon

    @lon.setter
    def lon(self, lon: float):
        """Sets the lon of this Station.

        Longitude  # noqa: E501

        :param lon: The lon of this Station.
        :type lon: float
        """

        self._lon = lon