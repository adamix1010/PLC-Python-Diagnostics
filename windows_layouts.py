import PySimpleGUI as Sg

Sg.theme('DarkAmber')

# Start Window
layout_s = [[Sg.Text('Enter settings of S7 Controller:')],
            [Sg.Text('PLC Address:', size=(15, 1)), Sg.InputText()],
            [Sg.Text('PLC Rack:', size=(15, 1)), Sg.InputText()],
            [Sg.Text('PLC Slot:', size=(15, 1)), Sg.InputText()],
            [Sg.Text('DB Address:', size=(15, 1)), Sg.InputText()],
            [Sg.Submit(), Sg.Cancel()]
            ]

# Process Window
layout_w = [
    [Sg.Text('Diagnostic Data:')],
    [Sg.Text('PLC to PC:', size=(20, 1)), Sg.Text('PC to PLC:', size=(20, 1))],
    [Sg.Text('Bool Data:', size=(20, 1)), Sg.Text('Bool Data:', size=(20, 1))],
    [Sg.Text('0.0', size=(3, 1)), Sg.Text('0', key='out_0_0', size=(5, 1), text_color='Green'),
     Sg.Text('0.1', size=(3, 1)), Sg.Text('0', key='out_0_1', size=(4, 1), text_color='Green'),
     Sg.Text('0.0', size=(3, 1)), Sg.Checkbox("0", default=False, key='in_0_0', size=(8, 1)),
     Sg.Text('0.1', size=(3, 1)),
     Sg.Checkbox("0", default=False, key='in_0_1', size=(8, 1))
     ],
    [Sg.Text('0.2', size=(3, 1)), Sg.Text('0', key='out_0_2', size=(5, 1), text_color='Green'),
     Sg.Text('0.3', size=(3, 1)), Sg.Text('0', key='out_0_3', size=(4, 1), text_color='Green'),
     Sg.Text('0.2', size=(3, 1)), Sg.Checkbox("0", default=False, key='in_0_2', size=(8, 1)),
     Sg.Text('0.3', size=(3, 1)),
     Sg.Checkbox("0", default=False, key='in_0_3', size=(8, 1))
     ],
    [Sg.Text('0.4', size=(3, 1)), Sg.Text('0', key='out_0_4', size=(5, 1), text_color='Green'),
     Sg.Text('0.5', size=(3, 1)), Sg.Text('0', key='out_0_5', size=(4, 1), text_color='Green'),
     Sg.Text('0.4', size=(3, 1)), Sg.Checkbox("0", default=False, key='in_0_4', size=(8, 1)),
     Sg.Text('0.5', size=(3, 1)),
     Sg.Checkbox("0", default=False, key='in_0_5', size=(8, 1))
     ],
    [Sg.Text('0.6', size=(3, 1)), Sg.Text('0', key='out_0_6', size=(5, 1), text_color='Green'),
     Sg.Text('0.7', size=(3, 1)), Sg.Text('0', key='out_0_7', size=(4, 1), text_color='Green'),
     Sg.Text('0.6', size=(3, 1)), Sg.Checkbox("0", default=False, key='in_0_6', size=(8, 1)),
     Sg.Text('0.7', size=(3, 1)),
     Sg.Checkbox("0", default=False, key='in_0_7', size=(8, 1))
     ],
    [Sg.Text('1.0', size=(3, 1)), Sg.Text('0', key='out_1_0', size=(5, 1), text_color='Green'),
     Sg.Text('1.1', size=(3, 1)), Sg.Text('0', key='out_1_1', size=(4, 1), text_color='Green'),
     Sg.Text('1.0', size=(3, 1)), Sg.Checkbox("0", default=False, key='in_1_0', size=(8, 1)),
     Sg.Text('1.1', size=(3, 1)),
     Sg.Checkbox("0", default=False, key='in_1_1', size=(8, 1))
     ],
    [Sg.Text('1.2', size=(3, 1)), Sg.Text('0', key='out_1_2', size=(5, 1), text_color='Green'),
     Sg.Text('1.3', size=(3, 1)), Sg.Text('0', key='out_1_3', size=(4, 1), text_color='Green'),
     Sg.Text('1.2', size=(3, 1)), Sg.Checkbox("0", default=False, key='in_1_2', size=(8, 1)),
     Sg.Text('1.3', size=(3, 1)),
     Sg.Checkbox("0", default=False, key='in_1_3', size=(8, 1))
     ],
    [Sg.Text('1.4', size=(3, 1)), Sg.Text('0', key='out_1_4', size=(5, 1), text_color='Green'),
     Sg.Text('1.5', size=(3, 1)), Sg.Text('0', key='out_1_5', size=(4, 1), text_color='Green'),
     Sg.Text('1.4', size=(3, 1)), Sg.Checkbox("0", default=False, key='in_1_4', size=(8, 1)),
     Sg.Text('1.5', size=(3, 1)),
     Sg.Checkbox("0", default=False, key='in_1_5', size=(8, 1))
     ],
    [Sg.Text('1.6', size=(3, 1)), Sg.Text('0', key='out_1_6', size=(5, 1), text_color='Green'),
     Sg.Text('1.7', size=(3, 1)), Sg.Text('0', key='out_1_7', size=(4, 1), text_color='Green'),
     Sg.Text('1.6', size=(3, 1)), Sg.Checkbox("0", default=False, key='in_1_6', size=(8, 1)),
     Sg.Text('1.7', size=(3, 1)),
     Sg.Checkbox("0", default=False, key='in_1_7', size=(8, 1))
     ],
    [Sg.Text('Int Data:', size=(20, 1)), Sg.Text('Int Data:', size=(20, 1))],
    [Sg.Text('0', size=(3, 1)), Sg.Text(key='out_int_0', size=(5, 1), text_color='Green'),
     Sg.Text('1', size=(3, 1)), Sg.Text(key='out_int_1', size=(4, 1), text_color='Green'),
     Sg.Text('0', size=(3, 1)), Sg.InputText(key='in_int_0', size=(8, 1)), Sg.Text('1', size=(3, 1)),
     Sg.InputText(key='in_int_1', size=(8, 1))
     ],
    [Sg.Text('2', size=(3, 1)), Sg.Text(key='out_int_2', size=(5, 1), text_color='Green'),
     Sg.Text('3', size=(3, 1)), Sg.Text(key='out_int_3', size=(4, 1), text_color='Green'),
     Sg.Text('2', size=(3, 1)), Sg.InputText(key='in_int_2', size=(8, 1)), Sg.Text('3', size=(3, 1)),
     Sg.InputText(key='in_int_3', size=(8, 1))
     ],
    [Sg.Text('4', size=(3, 1)), Sg.Text(key='out_int_4', size=(5, 1), text_color='Green'),
     Sg.Text('5', size=(3, 1)), Sg.Text(key='out_int_5', size=(4, 1), text_color='Green'),
     Sg.Text('4', size=(3, 1)), Sg.InputText(key='in_int_4', size=(8, 1)), Sg.Text('5', size=(3, 1)),
     Sg.InputText(key='in_int_5', size=(8, 1))
     ],
    [Sg.Text('6', size=(3, 1)), Sg.Text(key='out_int_6', size=(5, 1), text_color='Green'),
     Sg.Text('7', size=(3, 1)), Sg.Text(key='out_int_7', size=(4, 1), text_color='Green'),
     Sg.Text('6', size=(3, 1)), Sg.InputText(key='in_int_6', size=(8, 1)), Sg.Text('7', size=(3, 1)),
     Sg.InputText(key='in_int_7', size=(8, 1))
     ],
    [Sg.Text('8', size=(3, 1)), Sg.Text(key='out_int_8', size=(5, 1), text_color='Green'),
     Sg.Text('9', size=(3, 1)), Sg.Text(key='out_int_9', size=(4, 1), text_color='Green'),
     Sg.Text('8', size=(3, 1)), Sg.InputText(key='in_int_8', size=(8, 1)), Sg.Text('9', size=(3, 1)),
     Sg.InputText(key='in_int_9', size=(8, 1))
     ],
    [Sg.Text('String Data:', size=(20, 1)), Sg.Text('String Data:', size=(20, 1))],
    [Sg.Text(size=(24, 1), key='out_str_0'), Sg.InputText(key='in_str_0', size=(24, 1))],
    [Sg.Submit(), Sg.Cancel()]
]
