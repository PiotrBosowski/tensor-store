import numpy as np
import math

from array import array
from os.path import join

with open(join('..', '.cache', 'file'), 'wb') as output_file:
    type_array = array('I', [1])
    type_array.tofile(output_file)
    rank_array = array('I', [3])
    rank_array.tofile(output_file)
    dims_array = array('I', [3, 2, 2])
    dims_array.tofile(output_file)
    data_array = array('f', [1., 2., 3.,
                             4., 5., 6.,
                             7., 8., 9.,
                             10., 11., 12.])
    data_array.tofile(output_file)
    output_file.close()

with open(join('..', '.cache', 'file'), 'rb') as input_file:
    type_array = array('I')
    type_array.fromstring(input_file.read(4))
    rank_array = array('I')
    rank_array.fromstring(input_file.read(4))
    rank = rank_array[0]
    dims_array = array('I')
    dims_array.fromstring(input_file.read(4 * rank))
    data_array = array('f')
    items_count = math.prod(dims_array)
    data_array.fromstring(input_file.read(4 * items_count))
    result = np.array(data_array).reshape(dims_array)
    print(result)
    stp_dbg = 0
