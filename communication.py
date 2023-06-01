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


def read_int(client, db_number: int, start: int):
    read = client.db_read(db_number, start, 2)
    result = snap7.util.get_int(read, 0)
    return result


def write_int(client, db_number: int, start: int, int_value: int):
    read = client.db_read(db_number, start, 2)
    snap7.util.set_int(read, 0, int_value)
    client.db_write(db_number, start, read)


def read_string(client, db_number: int, start: int):
    read = client.db_read(db_number, start, 22)
    result = snap7.util.get_string(read, 0)
    return result


def write_string(client, db_number: int, start: int, str_value: str, max_size: int):
    read = client.db_read(db_number, start, 22)
    snap7.util.set_string(read, 0, str_value, max_size)
    client.db_write(db_number, start, read)

