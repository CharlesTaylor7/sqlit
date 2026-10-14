"""
for declaring lsp classes
names are one for one with microsoft.
Uses: LSP version 3.18
https://microsoft.github.io/language-server-protocol/specifications/lsp/3.18/specification/
"""

from dataclasses import dataclass
from typing import ClassVar, Type, TypedDict, Union, Any, Literal, Optional
from dataclass_wizard import JSONWizard


@dataclass
class InitializeParams:
    class Meta(JSONWizard.Meta):
        tag = "initialize"

    Point2D: ClassVar = TypedDict("", {"xy": int, "y": int, "label": str})
    workspaceFolders: list[Point2D]
    capabilities: ClientCapabilities


@dataclass
class InitializeResult:
    class Meta(JSONWizard.Meta):
        tag = "initialize"

    capabilities: ServerCapabilities | None = None
    serverInfo: ServerInfo | None = None


# BEGIN Type definitions & aliases

URI = str
string = str

PositionEncoding = Literal["utf-8", "utf-16", "utf-32"]


@dataclass
class ServerInfo:
    name: string
    version: string | None = None


@dataclass
class WorkspaceFolder:
    uri: URI
    name: string


@dataclass
class ClientCapabilities:
    general: GeneralClientCapabilities
    pass


@dataclass
class GeneralClientCapabilities:
    positionEncodings: list[PositionEncoding] | None
    pass


@dataclass
class ServerCapabilities:
    positionEncoding: PositionEncoding = "utf-16"
    pass


# union of all lsp param types
LspParams = InitializeParams
LspResult = InitializeResult
__all__ = ["LspParams"]
