import traceback
from pathlib import Path
from typing import AnyStr, BinaryIO, Union, cast
from io import TextIOWrapper
import socket
from sys import stdin, stdout
import json
from dataclasses import dataclass
from dataclass_wizard import JSONWizard
from . import lsp
from . import jsonrpc


def main():
    run_socket()


def run_socket():
    socket_path = ".nvim/goose.sock"
    Path(socket_path).unlink(missing_ok=True)

    # 1. Delete the file if it already exists
    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as server:
        server.bind(socket_path)
        server.listen()

        while True:
            connection, _ = server.accept()
            with connection.makefile(mode="rwb") as io:
                loop(io, io)  # pyright: ignore


def run_stdio():
    loop(stdin.buffer, stdout.buffer)


def handle_next(input: BinaryIO, output: BinaryIO):
    while True:
        header = input.readline()
        if header.startswith(b"Content-Type:"):
            continue

        if header.startswith(b"Content-Length:"):
            _, raw_byte_count = header.split(b"Content-Length: ")
            byte_count = int(raw_byte_count)
            continue

        if header == b"\r\n":
            request = input.read(byte_count)
            parsed = jsonrpc.Request.from_json(request)
            cast(jsonrpc.Request, parsed)
            print(parsed)
            return


def loop(input: BinaryIO, output: BinaryIO):
    while True:
        try:
            handle_next(input, output)

        except Exception:
            traceback.print_exc()
