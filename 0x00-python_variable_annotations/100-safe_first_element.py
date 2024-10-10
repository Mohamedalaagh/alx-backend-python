#!/usr/bin/env python3
"""Augment the following code with correct duck-typed annotations:

# The types of the elements of the input are not know
def safe_first_element(ls):
    if ls:
        return ls[0]
    else:
        return None

{'ls': typing.Sequence[typing.Any], 'return': \
    typing.Union[typing.Any, NoneType]}
"""


import typing


def safe_first_element(lst: typing.Sequence[typing.Any]) -> \
        typing.Union[typing.Any, None]:
    """annotation"""
    if lst:
        return lst[0]
    else:
        return None
