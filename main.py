import numpy as np

from array import array

with open('file', 'wb') as output_file:
    float_array = array('f', [3.14, 2.7, -1.0, 1.1, 128, 15, 11])
    float_array.tofile(output_file)
    output_file.close()

with open('file', 'rb') as input_file:
    a = input_file.read(4)
    float_array = array('f')
    float_array.fromstring(input_file.read())
    print(float_array)

    b = np.array(float_array)

    stp_dbg = 0
