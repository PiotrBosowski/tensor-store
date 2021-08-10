import struct

bytes_to_write = [128, 0, 0, 5]


with open("filename.txt", "wb") as file:
    byte_array = bytearray(bytes_to_write)
    file.write(byte_array)

with open('filename.txt', 'rb') as file:
    liczba = 5
    red = file.read()
    result = struct.unpack('i', red)
    for item in file:
        print(item)
