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

print()

# metadata block
for i in range(3):
    result_dict = read_mdb(f)

    print("block type:", mdb_type[result_dict['block_type']])
    print(result_dict)
    if result_dict['last_mdb_flag']:
        print("\nLAST metadata block")

    print("\n*****\n")

print((f.read(4)).hex())
