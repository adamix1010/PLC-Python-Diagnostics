import re
import PySimpleGUI as sg
import snap7
from communication import read_bool, write_bool
from windows_layouts import layout_s, layout_w


# Create the Window
window_S = sg.Window('AD S7 Diagnostics', layout_s)
while True:
    event_S, values_S = window_S.read()
    # Check if address is valid
    if event_S == 'Cancel' or event_S == sg.WIN_CLOSED:
        window_S.close()
        quit()
    elif event_S == 'Submit':
        ip_check = re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", values_S[0])
        if ip_check is None:
            print('Ip address not valid')
            sg.popup('Ip address is not valid')
            event_S = 'B'
        else:
            window_S.close()
            break
window_S.close()

# Create PLC connection
s7 = snap7.client.Client()
s7.connect(values_S[0], int(values_S[1]), int(values_S[2]))
DB_ADDRESS = int(values_S[3])

# Create main window
window = sg.Window(title="AD S7 Diagnostics", layout=layout_w)

while True:
    # --------- Read and update window --------
    event, values = window.read(timeout=10)
    window.refresh()
    read = read_bool(s7, DB_ADDRESS, 64, 2)
    for i in range(0, 8):
        window[f'out_{i}'].Update(read[0, i])
    if event == 'Submit':
        for i in range(0, 8):
            write = write_bool(s7, 2, 0, DB_ADDRESS, 0, i, values[f'in_{i}'])
        read_out = read_bool(s7, DB_ADDRESS, 0, 2)
        for i in range(0, 8):
            window[f'in_{i}'].Update(text=read_out[0, i])
    if event == sg.WIN_CLOSED or event == 'Cancel':
        window.close()
        break

read = read_bool(s7, 2, 64, 2)
print(read)
write = write_bool(s7, 2, 0, 2, 0, 0, True)
print(write)
