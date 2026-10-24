import inspect
from dataclasses import fields, is_dataclass
from enum import Enum
from types import NoneType
from typing import (
    Any,
    ForwardRef,
    Literal,
    Type,
    TypeAliasType,
    Union,
    TYPE_CHECKING,
    TypeAlias,
)
import typing

if TYPE_CHECKING:
    from _typeshed import DataclassInstance
from goose.lsp import (
    CallHierarchyIncomingCall,
    GeneralClientCapabilities,
    PositionEncodingKind,
)


def deserialize[T](type: type[T], data) -> T:
    if typing.get_origin(type) == Literal:
        if typing.get_args(type)[0] == data:
            return data  # type: ignore
        else:
            raise Exception("Literal doesn't match data")

    if isinstance(type, TypeAliasType):
        return deserialize(type.__value__, data)

    if isinstance(type, ForwardRef):
        return deserialize(type.evaluate(), data)

    if typing.get_origin(type) == Union:
        return deserialize_union(type, data)

    if is_dataclass(type):
        return deserialize_dict(type, data)  # type: ignore

    if inspect.isclass(type) and issubclass(type, Enum):
        return deserialize_enum(type, data)  # type: ignore

    if typing.get_origin(type) == list:  # type: ignore
        return deserialize_list(typing.get_args(type)[0], data)  # type: ignore

    if type == str and isinstance(data, str):
        return data  # type: ignore

    if type == int and isinstance(data, int):
        return data  # type: ignore

    if type == float and isinstance(data, float):
        return data  # type: ignore

    if type == bool and isinstance(data, bool):
        return data  # type: ignore

    if type == Any:
        return data  # type: ignore

    print(f"{type=}, {data=}")
    raise NotImplementedError


def deserialize_union[T](type: type[T], data) -> T:
    union_args = typing.get_args(type)
    is_optional = NoneType in union_args
    if data is None:
        if is_optional:
            return None  # type: ignore
        else:
            raise Exception("None found for required data")

    if len(union_args) > 2 or not is_optional:
        for arg in union_args:
            try:
                return deserialize(arg, data)
            except:
                pass

        raise NotImplementedError
    else:
        return deserialize(union_args[0], data)  # type: ignore


def deserialize_enum[T: Enum](type: type[T], data: str | int) -> T:
    return type(data)


def deserialize_list[T](type: type[T], data: list) -> list[T]:
    return [deserialize(type, item) for item in data]


def deserialize_dict[T: DataclassInstance](type: type[T], data: dict[str, Any]) -> T:
    result = type.__new__(type)  # type: ignore

    for field in fields(type):
        if "json" in field.metadata:
            data[field.name] = data.pop(field.metadata["json"])

        if field.name in data:
            data[field.name] = deserialize(field.type, data[field.name])  # type: ignore

    result.__init__(**data)

    return result
