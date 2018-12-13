import os

file = 'test.flac'
#file = 'README.md'

# fileサイズ(byte)
size = os.path.getsize(file)

# 区切りバイト数、改行バイト数
delimiter_num = 4
newline_num = 16
