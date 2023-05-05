import snap7
import numpy as np


def read_bool(client, db_number: int, start: int, size: int):
    read = client.db_read(db_number, start, size)
    result = np.flip(np.unpackbits(read).reshape(size, 8), 1)
    return result


def write_bool(client, db_number: int, start: int, size: int, byte_idx: int, bool_idx: int, bool_val: bool):
    read = client.db_read(db_number, start, size)
    snap7.util.set_bool(read, byte_idx, bool_idx, bool_val)
    client.db_write(db_number, start, read)
    read = read_bool(client, db_number, start, size)
    if read[byte_idx, bool_idx] == bool_val:
        return '1'
    else:
        return '0'
