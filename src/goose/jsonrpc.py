"""
for declaring jsonrpc classes & utilities
https://www.jsonrpc.org/specification
"""

from ast import And
from dataclasses import dataclass
from typing import Union, Any, Literal, Optional
from dataclass_wizard import JSONWizard
from typing import TYPE_CHECKING

from goose.lsp import LspParams


# https://www.jsonrpc.org/specification#request_object
@dataclass
class Request(JSONWizard):
    jsonrpc: Literal["2.0"]
    method: str
    params: Optional[LspParams]
    id: Union[str, int, None]

    class Meta(JSONWizard.Meta):
        tag_key = "method"


# https://www.jsonrpc.org/specification#response_object
@dataclass
class Response(JSONWizard):
    jsonrpc: Literal["2.0"]
    result: Optional[dict]  # TODO: result types
    error: Optional[Error]
    id: Union[str, int, None]


# https://www.jsonrpc.org/specification#error_object
@dataclass
class Error(JSONWizard):
    code: int
    message: str
    data: Optional[Any]
