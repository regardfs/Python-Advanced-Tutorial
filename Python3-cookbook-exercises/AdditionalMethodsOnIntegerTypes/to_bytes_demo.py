# Return an array of bytes representing an integer.
(1024).to_bytes(2, byteorder='big')
# return b'\x04\x00'

(1024).to_bytes(10, byteorder='little')
# return b'\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00'

(1024).to_bytes(10, byteorder='big') # equals to (1024).to_bytes(10, byteorder='big', signed=True)
# return b'\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00'

(-1024).to_bytes(10, byteorder='big', signed=True)
#