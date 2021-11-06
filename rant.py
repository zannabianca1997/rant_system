from enum import Enum, auto
from typing import Any, Dict, List, Tuple
from dataclasses import dataclass

from json import dumps, loads
from base64 import b64encode, b64decode
from hashlib import sha256

from zipfile import ZipFile


class Format(Enum):
    plaintext = auto()
    markdown = auto()


Patch = Dict[str, Any]


@dataclass
class Diff:
    timestamp: int
    patches: List[Patch]
    last_hash: bytes

    def to_dict(self) -> Dict[str, Any]:
        return {
            "timestamp": self.timestamp,
            "patches": self.patches,
            "last_hash": b64encode(self.last_hash).decode("utf-8")
        }

    def bhash(self):
        return sha256(
            dumps(
                self.to_dict(),
                sort_keys=True,
                separators=(',', ':')
            )
        ).digest()

    def __str__(self) -> str:
        return dumps(
            self.to_dict(),
            indent=4,
            sort_keys=True
        )


class Rant:
    _rnt_version: Tuple[int, int]
    _title: str
    _format: Format
    _content: str

    _incoming_patches: List[Patch]
    _history: List[Diff]

    def __init__(self, inp: ZipFile) -> None:
        #todo: parse the rnt file
        raise NotImplementedError()
        _incoming_patches = []

    def write_out(self, out: ZipFile) -> None:
        #todo: write out the rnt file
        raise NotImplementedError()

    def confirm_patches(self, timestamp: int):
        #todo: check that timestamp is > to the last. if equal, merge the two
        self._history.append(
            Diff(
                timestamp,
                self._incoming_patches,
                self._history[-1].bhash()
            )
        )
        self._incoming_patches = []
    
    #todo: implement all modifing action as property, adding patches
