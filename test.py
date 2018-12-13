import os
import struct
import sys
from funcs import *

file = 'test.flac'
#file = 'README.md'
f = open(file, 'rb')
size = os.path.getsize(file)



# f.seek(offset, from_what)
# from_what:
# 0: ファイルの先頭から
# 1: 現在のファイル位置から
# 2: ファイルの終端から


# 10進数を2進数へ
# bin(5) => '0b101'



# &: and
# |: or
# ^: xor


# >>> int.from_bytes(b'\x00\x10', 'little')
# 4096
# >>> int.from_bytes(b'\x00\x10', 'big')
# 16


# bytes型から16進表記のstring型を取得
# b'\x00\x10'.hex()


# 特定のバイトに対し、処理したいとき
# if b == b'\x3d':
#     print(b)
