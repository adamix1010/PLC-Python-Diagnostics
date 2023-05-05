import PySimpleGUI as sg

sg.theme('DarkAmber')

# Start Window
layout_s = [[sg.Text('Enter settings of S7 Controller:')],
            [sg.Text('PLC Address:', size=(15, 1)), sg.InputText()],
            [sg.Text('PLC Rack:', size=(15, 1)), sg.InputText()],
            [sg.Text('PLC Slot:', size=(15, 1)), sg.InputText()],
            [sg.Text('DB Address:', size=(15, 1)), sg.InputText()],
            [sg.Submit(), sg.Cancel()]
            ]

# Process Window
layout_w = [
    [sg.Text('Diagnostic Data:')],
    [sg.Text('PLC to PC:', size=(20, 1)), sg.Text('PC to PLC:', size=(20, 1))],
    [sg.Text('Bool Data:', size=(20, 1)), sg.Text('Bool Data:', size=(20, 1))],
    [sg.Text('0.0', size=(3, 1)), sg.Text('0', key='out_0', size=(5, 1), text_color='Green'),
     sg.Text('0.1', size=(3, 1)), sg.Text('0', key='out_1', size=(4, 1), text_color='Green'),
     sg.Text('0.0', size=(3, 1)), sg.Checkbox("0", default=False, key='in_0', size=(8, 1)), sg.Text('0.1', size=(3, 1)),
     sg.Checkbox("0",default=False, key='in_1', size=(8, 1))
     ],
    [sg.Text('0.2', size=(3, 1)), sg.Text('0', key='out_2', size=(5, 1), text_color='Green'),
     sg.Text('0.3', size=(3, 1)), sg.Text('0', key='out_3', size=(4, 1), text_color='Green'),
     sg.Text('0.2', size=(3, 1)), sg.Checkbox("0",default=False, key='in_2', size=(8, 1)), sg.Text('0.3', size=(3, 1)),
     sg.Checkbox("0", default=False, key='in_3', size=(8, 1))
     ],
    [sg.Text('0.4', size=(3, 1)), sg.Text('0', key='out_4', size=(5, 1), text_color='Green'),
     sg.Text('0.5', size=(3, 1)), sg.Text('0', key='out_5', size=(4, 1), text_color='Green'),
     sg.Text('0.4', size=(3, 1)), sg.Checkbox("0",default=False, key='in_4', size=(8, 1)), sg.Text('0.5', size=(3, 1)),
     sg.Checkbox("0", default=False, key='in_5', size=(8, 1))
     ],
    [sg.Text('0.6', size=(3, 1)), sg.Text('0', key='out_6', size=(5, 1), text_color='Green'),
     sg.Text('0.7', size=(3, 1)), sg.Text('0', key='out_7', size=(4, 1), text_color='Green'),
     sg.Text('0.6', size=(3, 1)), sg.Checkbox("0",default=False, key='in_6', size=(8, 1)), sg.Text('0.7', size=(3, 1)),
     sg.Checkbox("0", default=False, key='in_7', size=(8, 1))
     ],
    [sg.Submit(), sg.Cancel()]
]