import inspect
from dataclasses import fields, is_dataclass
from enum import Enum
from typing import Any, Type, TYPE_CHECKING

if TYPE_CHECKING:
    from _typeshed import DataclassInstance
from goose.lsp import (
    CallHierarchyIncomingCall,
    GeneralClientCapabilities,
    PositionEncodingKind,
)


type JsonAny = JsonObject | JsonArray | str | int | float | bool | None
type JsonObject = dict[str, JsonAny]
type JsonArray = list[JsonAny]


def deserialize[T](type: type[T], data: JsonAny) -> T:
    if is_dataclass(type):
        return deserialize_dict(type, data)  # pyright: ignore

    if inspect.isclass(type) and issubclass(type, Enum):
        return deserialize_enum(type, data)  # pyright: ignore

    if type.__origin__ == list:  # pyright: ignore
        return deserialize_list(type, data)  # pyright: ignore

    raise NotImplementedError


def deserialize_enum[T: Enum](type: type[T], data: str | int) -> T:
    return type(data)


def deserialize_list[T](type: type[T], data: list[JsonAny]) -> list[T]:
    return [deserialize(type, item) for item in data]


def deserialize_dict[T: DataclassInstance](
    type: type[T], data: dict[str, JsonAny]
) -> T:
    result = type.__new__(type)  # pyright: ignore

    for field in fields(type):
        if "json" in field.metadata:
            data[field.name] = data.pop(field.metadata["json"])

        # recurse dataclasses, but not collections or primitives
        if is_dataclass(field.type):
            data[field.name] = deserialize_dict(field.type, data[field.name])  # pyright: ignore

    result.__init__(**data)

    return result


print(deserialize(list[PositionEncodingKind], ["utf-8"]))

print(
    deserialize(
        GeneralClientCapabilities,
        {
            "markdown": 3,
            "positionEncodings": ["2"],
        },
    )
)
