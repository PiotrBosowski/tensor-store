import timeit
import numpy as np
import math

from array import array
from os.path import join


def tensorstore_save_read(tensor: np.array):
    with open(join('..', '.cache', 'file'), 'wb') as output_file:
        type_array = array('I', [1])
        type_array.tofile(output_file)
        rank_array = array('I', [tensor.ndim])
        rank_array.tofile(output_file)
        dims_array = array('I', tensor.shape)
        dims_array.tofile(output_file)
        data_array = array('f', tensor.reshape(-1))
        data_array.tofile(output_file)
        output_file.close()

    with open(join('..', '.cache', 'file'), 'rb') as input_file:
        type_array = array('I')
        type_array.frombytes(input_file.read(4))
        rank_array = array('I')
        rank_array.frombytes(input_file.read(4))
        rank = rank_array[0]
        dims_array = array('I')
        dims_array.frombytes(input_file.read(4 * rank))
        data_array = array('f')
        items_count = math.prod(dims_array)
        data_array.frombytes(input_file.read(4 * items_count))
        tensor_read = np.array(data_array).reshape(dims_array)
        assert np.array_equal(tensor, tensor_read)


def numpy_save_read(tensor: np.array):
    np.save(join('..', '.cache', 'file.npy'), tensor)
    tensor_read = np.load(join('..', '.cache', 'file.npy'))
    assert np.array_equal(tensor, tensor_read)


if __name__ == '__main__':
    iterations = 1
    tensor = np.zeros((10000000))

    numpy_time = timeit.timeit(
        lambda: numpy_save_read(tensor), number=iterations)
    print('numpy: ', numpy_time)

    tensor_store_time = timeit.timeit(
        lambda: tensorstore_save_read(tensor), number=iterations)
    print('tensor-store: ', tensor_store_time)

    stp_dbg = 0
