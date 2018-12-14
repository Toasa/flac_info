from setting import *

def is_flac(f):
    b = f.read(4)
    if b.decode() == 'fLaC':
        return True
    return False

def print_nbyte(b, n):
    for i in range(n):
        if (i+1) % newline_num == 0:
            # ここを変更する、b[i]的な
            print(hex(b[i]))
        elif (i+1) % delimiter_num == 0:
            print(hex(b[i]), '| ', end='')
        else:
            print(hex(b[i]), '', end='')
    print()

def read_mdb(f):
    d = read_mdb_header(f)
    type = d['block_type']

    if type == STREAMINFO:
        d1 = read_streaminfo(f)
        d.update(d1)
    elif type == PADDING:
        f.read(d['len_md'])
    elif type == VORBIS_COMMENT:
        comment_len = d['len_md']
        b = f.read(comment_len)
        d["VORBIS_COMMENT"] = b.hex()
        #print_nbyte(b, comment_len)
    elif type == 127:
        print(invalid_type)
        sys.exit()
    else:
        b = f.read(d['len_md'])
        #d["?"] = b

    return d

def read_mdb_header(f):
    # return dict
    d = {}

    b = f.read(1)

    if BtoI(b) & 0b10000000 != 0:
        # 最上位bitが立っているとき
        last_mdb_flag = True
    else:
        last_mdb_flag = False
    d['last_mdb_flag'] = last_mdb_flag

    d['block_type'] = BtoI(b) & 0b01111111

    d['len_md'] = BtoI(f.read(3))

    return d

def read_streaminfo(f):
    # return dict
    d = {}
    d['min_block_size'] = BtoI(f.read(2))
    d['max_block_size'] = BtoI(f.read(2))
    d['min_flame_size'] = BtoI(f.read(3))
    d['max_flame_size'] = BtoI(f.read(3))

    b = f.read(8)
    d['rate'] = (BtoI(b) >> 44)

    # 後ろの3bit(7=0b111)のみ抽出する
    d['ch_num'] = ((BtoI(b) >> 41) & 7) + 1

    # bit per sample, 後ろの5bit(31=0b11111)のみ抽出する
    d['bps'] = (BtoI(b) >> 36) & 31

    # (2**36 - 1): 0から36個のビットが立っている数
    d['total_samples'] = BtoI(b) & (2**36 - 1)

    #d['md5'] = BtoI(f.read(16))
    d['md5'] = f.read(16).hex()

    return d

# convert bytes to integer in big endian notation
def BtoI(b):
    return int.from_bytes(b, 'big')
