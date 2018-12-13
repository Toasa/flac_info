from setting import *

def is_flac(f):
    b = f.read(4)
    if b.decode() == 'fLaC':
        return True
    return False

def print_nbyte(f, n):
    for i in range(n):
        b = f.read(1)

        if (i+1) % newline_num == 0:
            print(b.hex())
        elif (i+1) % delimiter_num == 0:
            print(b.hex(), '| ', end='')
        else:
            print(b.hex(), '', end='')
    print()

def read_mdb(f):
    result = read_mdb_header(f)

    #read_mdb_data(f)
    return result

def read_mdb_header(f):
    b = f.read(1)
    if int.from_bytes(b, 'big') & 0b10000000 != 0:
        # 最上位bitが立っているとき
        last_mdb_flag = True
    else:
        last_mdb_flag = False

    block_type = int.from_bytes(b, 'big') & 0b01111111

    len_md = int.from_bytes(f.read(3), 'big')

    return last_mdb_flag, block_type, len_md
