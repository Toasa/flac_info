import os

# sample rate = 8000KHz
# 1: モノラル、2: ステレオ
# channel num = 2
file = 'test.flac'

# fileサイズ(byte)
size = os.path.getsize(file)

# 区切りバイト数、改行バイト数
delimiter_num = 4
newline_num = 16


# md-block_type
mdb_type = ['STREAMINFO', 'PADDING', 'APPLICATION'\
,'SEEKTABLE', 'VORBIS_COMMENT', 'CUESHEET', 'PICTURE']
# mdb_type[127] = 'invalid'


STREAMINFO = 0
PADDING = 1
APPLICATION = 2
SEEKTABLE = 3
VORBIS_COMMENT = 4
CUESHEET = 5
PICTURE = 6
