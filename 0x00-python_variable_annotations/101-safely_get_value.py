#!/usr/bin/env python3
"""Given the parameters and the returns values, add type
annotations to function

Hint: look at TypeVar

def safely_get_value(dict, key, default = None):
    if key in dict:
        return dict[key]
    else:
        return default
"""


import typing


T = typing.TypeVar('T')


def safely_get_value(dct: typing.Mapping, key: typing.Any, default:
                     typing.Union[T, None] = None) -> \
        typing.Union[typing.Any, T]:
    """annotations of function"""
    if key in dct:
        return dct[key]
    else:
        return default
