# This file is a part of IntelOwl https://github.com/intelowlproject/IntelOwl
# See the file 'LICENSE' for copying permission.

from django.db import models
import typing


class BaseChoices(models.TextChoices):
    @classmethod
    def aslist(cls) -> list:
        return [c for c in cls]

    @classmethod
    def as_type(cls) -> typing.Literal:
        return typing.Literal[cls.aslist()]


class TypeChoices(BaseChoices):
    FILE = "file"
    OBSERVABLE = "observable"


class HashChoices(BaseChoices):
    MD5 = "md5"
    SHA256 = "sha256"


class ObservableTypes(BaseChoices):
    IP = "ip"
    URL = "url"
    DOMAIN = "domain"
    HASH = "hash"
    GENERIC = "generic"
