# Return the integer represented by the given array of bytes.
int.from_bytes(b'\x00\x10', byteorder='big')
# return 16
int.from_bytes(b'\x00\x10', byteorder='little')
# return 4096
int.from_bytes(b'\xfc\x00', byteorder='big', signed=True)
# return -1024
int.from_bytes(b'\xfc\x00', byteorder='big', signed=False)
# return 64512
int.from_bytes([255, 0, 0], byteorder='big')
# return 16711680
