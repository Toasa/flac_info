import struct
import sys
from funcs import *
from setting import *

f = open(file, 'rb')


# 区切りバイト数、改行バイト数
#delimiter_num = 4
#newline_num = 16

if not is_flac(f):
    print("not flac")
    sys.exit()

# metadata block
result = read_mdb(f)

if result[0]:
    print("last metadata block")
else:
    print("Not last metadata block")

print("block type: ", result[1])

print_nbyte(f, result[2])
