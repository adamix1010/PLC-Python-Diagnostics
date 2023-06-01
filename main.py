import re
import PySimpleGUI as Sg
import snap7
import itertools
from communication import read_bool, write_bool, read_int, write_int, read_string, write_string
from windows_layouts import layout_s, layout_w

# Create the Window
window_S = Sg.Window('AD S7 Diagnostics', layout_s)
while True:
    event_S, values_S = window_S.read()
    # Check if address is valid
    if event_S == 'Cancel' or event_S == Sg.WIN_CLOSED:
        window_S.close()
        quit()
    elif event_S == 'Submit':
        ip_check = re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", values_S[0])
        if ip_check is None:
            print('Ip address not valid')
            Sg.popup('Ip address is not valid')
            event_S = 'B'
        else:
            # Try to connect
            try:
                s7 = snap7.client.Client()
                s7.connect(values_S[0], int(values_S[1]), int(values_S[2]))
                window_S.close()
                break
            except RuntimeError:
                Sg.popup("Connection can't be established")
                print("Error: Connection can't be established")
                event_S = 'B'
window_S.close()

# Write DB address
DB_ADDRESS = int(values_S[3])

# Create main window
window = Sg.Window(title="AD S7 Diagnostics", layout=layout_w)

while True:

    # Read and update window
    event, values = window.read(timeout=500)
    read = read_bool(s7, DB_ADDRESS, 44, 2)
    read_out = read_bool(s7, DB_ADDRESS, 0, 2)

    # Update "PLC to PC" section
    for n, i in itertools.product(range(0, 2), range(0, 8)):
        window[f'out_{n}_{i}'].Update(read[n, i])
        window[f'in_{n}_{i}'].Update(text=read_out[n, i])
    for i in (range(0, 10)):
        window[f'out_int_{i}'].Update(value=read_int(s7, 2, 46 + (2 * i)))
    window[f'out_str_0'].Update(value=read_string(s7, 2, 66))

    # Send data to PLC
    if event == 'Submit':
        # Boolean values
        for n, i in itertools.product(range(0, 2), range(0, 8)):
            write = write_bool(s7, 2, 0, DB_ADDRESS, n, i, values[f'in_{n}_{i}'])

        # Integer values
        for i in (range(0, 10)):
            text = values[f'in_int_{i}']
            if text == '':
                pass
            else:
                # Check if written value is integer
                try:
                    value = int(text)
                    write_int(s7, 2, 2 * i, value)
                except ValueError:
                    Sg.popup('Integer is not valid')
                    event = 'B'
                    break
            window[f'in_int_{i}'].Update(value=read_int(s7, 2, 2 * i))

        # String values
        value_str = values[f'in_str_0']

        # Check if string value is within boundaries
        if len(value_str) <= 20:
            write_string(s7, 2, 22, value_str, 20)
        elif len(value_str) > 20:
            Sg.popup('String out is too long')
            event = 'B'
        window[f'in_str_0'].Update(value=read_string(s7, 2, 22))

    # Handle connection lost
    if s7.get_connected() == 0:
        Sg.popup("Connection lost")
        window_S.close()
        break

    # Close the window
    if event == Sg.WIN_CLOSED or event == 'Cancel':
        window.close()
        break
