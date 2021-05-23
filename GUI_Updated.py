# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 21:44:21 2020

@author: USER
"""

import PySimpleGUI as sg
import numpy as np
from pickle import load

# ADD TITLE COLOUR ,title_color='white'
sg.theme('DefaultNoMoreNagging')	# Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Developed by Nhan D. Dao and Hoang D. Nguyen')],
            [sg.Text('University of Architecture, Ho Chi Minh City')],
            [sg.Text('Ho Chi Minh, Vietnam')],
            [sg.Text('Email: nhan.daodinh@uah.edu.vn')],
            #[sg.Text('Input parameters')],
            [sg.Frame(layout=[
            [sg.Text('SM-1s',size=(12, 1)),sg.InputText(key='-f1-'),sg.Text('g')],
            [sg.Text('SM-2s',size=(12, 1)), sg.InputText(key='-f2-'),sg.Text('g')],
            [sg.Text('SM-3s',size=(12, 1)), sg.InputText(key='-f3-'),sg.Text('g')],
            [sg.Text('SM-4s',size=(12, 1)), sg.InputText(key='-f4-'),sg.Text('g')],
            [sg.Text('SM-5s',size=(12, 1)), sg.InputText(key='-f5-'),sg.Text('g')],
            [sg.Text(u"\u03bc1",size=(12, 1)), sg.InputText(key='-f6-'),sg.Text('--')],
            [sg.Text(u"\u03bc2",size=(12, 1)), sg.InputText(key='-f7-'),sg.Text('--')],
            [sg.Text(u"\u03bc3",size=(12, 1)), sg.InputText(key='-f8-'),sg.Text('--')],
            [sg.Text("L1",size=(12, 1)), sg.InputText(key='-f9-'),sg.Text('m')],
            [sg.Text("L2",size=(12, 1)), sg.InputText(key='-f10-'),sg.Text('m')],
            [sg.Text("L3",size=(12, 1)), sg.InputText(key='-f11-'),sg.Text('m')],
            [sg.Text("d1",size=(12, 1)), sg.InputText(key='-f12-'),sg.Text('m')],
            [sg.Text("d2",size=(12, 1)), sg.InputText(key='-f13-'),sg.Text('m')],
                   
            [sg.Text('d3',size=(12, 1)),sg.InputText(key='-f14-'),sg.Text('m')]],title='Input parameters')],
            [sg.Frame(layout=[   
            [sg.Text('Maximum Displacement',size=(23, 1)), sg.InputText(key='-OP-',size=(32, 1)),sg.Text('m')]],title='Output')],
            [sg.Button('Predict'),sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Predicting Maximum Displacement of TPB Isolation Systems', layout)

filename = 'BestModel_XGB.sav'
loaded_model = load(open(filename, 'rb'))
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':	# if user closes window or clicks cancel
        break
    #window['-OP-'].update('Please fill all the input parameters')
    if event == 'Predict':
        #window['-OP-'].update(values[0])
        #break
        if values['-f1-'] == '' or values['-f2-'] == '' or values['-f3-'] == '' or values['-f4-'] == '' or values['-f5-'] == '' or values['-f6-'] == '' or values['-f7-'] == '' or values['-f8-'] == '' or values['-f9-'] == '' or values['-f10-'] == '' or values['-f11-'] == '' or values['-f12-'] == '' or values['-f13-'] == '' or values['-f14-'] == '':

            window['-OP-'].update('Please fill all the input parameters')

        else:

            x_test=np.array([[float(values['-f1-'])*9.81,float(values['-f2-'])*9.81, float(values['-f3-'])*9.81,float(values['-f4-'])*9.81,float(values['-f5-'])*9.81,values['-f6-'],values['-f7-'],values['-f8-'],values['-f9-'],values['-f10-'],values['-f11-'],values['-f12-'],values['-f13-'],values['-f14-']]])
            y_pred_disp = loaded_model.predict(x_test)
            window['-OP-'].update(np.round((y_pred_disp[0]),4))

window.close()
