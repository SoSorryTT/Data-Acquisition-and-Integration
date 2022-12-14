# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class BasinFull(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, basin_id: int=None, name: str=None, area: float=None):  # noqa: E501
        """BasinFull - a model defined in Swagger

        :param basin_id: The basin_id of this BasinFull.  # noqa: E501
        :type basin_id: int
        :param name: The name of this BasinFull.  # noqa: E501
        :type name: str
        :param area: The area of this BasinFull.  # noqa: E501
        :type area: float
        """
        self.swagger_types = {
            'basin_id': int,
            'name': str,
            'area': float
        }

        self.attribute_map = {
            'basin_id': 'basinId',
            'name': 'name',
            'area': 'area'
        }
        self._basin_id = basin_id
        self._name = name
        self._area = area

    @classmethod
    def from_dict(cls, dikt) -> 'BasinFull':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BasinFull of this BasinFull.  # noqa: E501
        :rtype: BasinFull
        """
        return util.deserialize_model(dikt, cls)

    @property
    def basin_id(self) -> int:
        """Gets the basin_id of this BasinFull.


        :return: The basin_id of this BasinFull.
        :rtype: int
        """
        return self._basin_id

    @basin_id.setter
    def basin_id(self, basin_id: int):
        """Sets the basin_id of this BasinFull.


        :param basin_id: The basin_id of this BasinFull.
        :type basin_id: int
        """

        self._basin_id = basin_id

    @property
    def name(self) -> str:
        """Gets the name of this BasinFull.


        :return: The name of this BasinFull.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this BasinFull.


        :param name: The name of this BasinFull.
        :type name: str
        """

        self._name = name

    @property
    def area(self) -> float:
        """Gets the area of this BasinFull.

        Total basin area in sq.km  # noqa: E501

        :return: The area of this BasinFull.
        :rtype: float
        """
        return self._area

    @area.setter
    def area(self, area: float):
        """Sets the area of this BasinFull.

        Total basin area in sq.km  # noqa: E501

        :param area: The area of this BasinFull.
        :type area: float
        """

        self._area = area
