#!/usr/bin/env python3
"""Write a type-annotated function sum_mixed_list
returns their sum as a float.
"""

import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """Return the sum of the list as a float"""
    return float(sum(mxd_lst))
