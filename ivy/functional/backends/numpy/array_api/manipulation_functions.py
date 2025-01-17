# global
import numpy as np
from typing import Union, Tuple, Optional, List


def roll(x: np.ndarray, shift: Union[int, Tuple[int]], axis: Union[int, Tuple[int]]=None)\
        -> np.ndarray:
    return np.roll(x, shift, axis)


def flip(x: np.ndarray,
         axis: Optional[Union[int, Tuple[int], List[int]]] = None)\
         -> np.ndarray:
    num_dims = len(x.shape)
    if not num_dims:
        return x
    if axis is None:
        axis = list(range(num_dims))
    if type(axis) is int:
        axis = [axis]
    axis = [item + num_dims if item < 0 else item for item in axis]
    return np.flip(x, axis)
