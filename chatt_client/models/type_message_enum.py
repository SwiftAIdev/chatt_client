# coding: utf-8

"""
    Chat Telegram Service API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class TypeMessageEnum(str, Enum):
    """
    TypeMessageEnum
    """

    """
    allowed enum values
    """
    TEXT = 'text'
    VIDEO = 'video'
    AUDIO = 'audio'
    IMAGE = 'image'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TypeMessageEnum from a JSON string"""
        return cls(json.loads(json_str))


