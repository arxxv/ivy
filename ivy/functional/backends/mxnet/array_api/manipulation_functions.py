# global
import mxnet as mx
from typing import Union, Tuple, Optional, List

# local
from ivy.functional.backends.mxnet import _handle_flat_arrays_in_out


def roll(x: mx.nd.ndarray.NDArray, shift: Union[int, Tuple[int]], axis: Union[int, Tuple[int]]=None) -> mx.nd.ndarray.NDArray:
    return mx.numpy.roll(x, shift, axis)


def flip(x: mx.ndarray.ndarray.NDArray,
         axis: Optional[Union[int, Tuple[int], List[int]]] = None)\
         -> mx.ndarray.ndarray.NDArray:
    num_dims = len(x.shape)
    if not num_dims:
        return x
    if axis is None:
        new_axis = list(range(num_dims))
    else:
        new_axis = axis
    if type(new_axis) is int:
        new_axis = [new_axis]
    else:
        new_axis = new_axis
    new_axis = [item + num_dims if item < 0 else item for item in new_axis]
    return mx.nd.flip(x, new_axis)
