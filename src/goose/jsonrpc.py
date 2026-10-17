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
