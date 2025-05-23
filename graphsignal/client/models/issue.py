# coding: utf-8

"""
    Graphsignal API

    API for uploading and querying spans, issues, metrics, and logs.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from graphsignal.client.models.tag import Tag
from typing import Optional, Set
from typing_extensions import Self

class Issue(BaseModel):
    """
    Issue
    """ # noqa: E501
    issue_id: Optional[StrictStr] = Field(default=None, description="Unique identifier for the issue.")
    span_id: Optional[StrictStr] = Field(default=None, description="The associated span identifier, if the issue is being associated with a span.")
    tags: Optional[List[Tag]] = Field(default=None, description="Tags associated with the issue.")
    name: StrictStr = Field(description="The name of the issue.")
    severity: Optional[StrictInt] = Field(default=None, description="Severity of the issue, 1-5 (info, low, medium, high, critical).")
    description: Optional[StrictStr] = Field(default=None, description="The description of the issue.")
    create_ts: StrictInt = Field(description="Unix timestamp (seconds) when the issue was created.")
    __properties: ClassVar[List[str]] = ["issue_id", "span_id", "tags", "name", "severity", "description", "create_ts"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Issue from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in tags (list)
        _items = []
        if self.tags:
            for _item_tags in self.tags:
                if _item_tags:
                    _items.append(_item_tags.to_dict())
            _dict['tags'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Issue from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "issue_id": obj.get("issue_id"),
            "span_id": obj.get("span_id"),
            "tags": [Tag.from_dict(_item) for _item in obj["tags"]] if obj.get("tags") is not None else None,
            "name": obj.get("name"),
            "severity": obj.get("severity"),
            "description": obj.get("description"),
            "create_ts": obj.get("create_ts")
        })
        return _obj


