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


# 10進数を2進数の文字列へ変換
# bin(5) => '0b101'
# hex(5) => '0x5'


f.seek(92, 0)
b = f.read(4)
print(b.hex()) => 81002000

81 00 20 00
bin(0x81) => '0b10000001'
0x2000 => 8192

# &: and
# |: or
# ^: xor


# >>> int.from_bytes(b'\x00\x10', 'little')
# 4096
# >>> int.from_bytes(b'\x00\x10', 'big')
# 16


# ２進数においてn桁のbitがすべてたったものが欲しい時
# bin(2**n - 1)


# bytes型から16進表記のstring型を取得
# b'\x00\x10'.hex()


# 特定のバイトに対し、処理したいとき
# if b == b'\x3d':
#     print(b)
