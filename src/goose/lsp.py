"""
for declaring lsp classes
names are one for one with microsoft.
Uses: LSP version 3.18
https://microsoft.github.io/language-server-protocol/specifications/lsp/3.18/specification/
"""

from ast import And
from dataclasses import dataclass
from typing import Union, Any, Literal, Optional
from dataclass_wizard import JSONWizard
from typing import TYPE_CHECKING


@dataclass
class InitializeParams:
    class Meta(JSONWizard.Meta):
        tag = "initialize"

    workspaceFolders: list[WorkspaceFolder] | None
    capabilities: ClientCapabilities


@dataclass
class InitializeResult:
    class Meta(JSONWizard.Meta):
        tag = "initialize"

    capabilities: ServerCapabilities
    serverInfo: ServerInfo


# BEGIN Type definitions & aliases

URI = str
string = str


@dataclass
class WorkspaceFolder:
    uri: URI
    name: string


@dataclass
class ClientCapabilities:
    pass


# union of all lsp param types
LspParams = InitializeParams
__all__ = ["LspParams"]
