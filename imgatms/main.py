#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import os.path

# Own librarys
""" import functions as f """
import imgatms.Utils.Date as d # Importo la clase Date
import imgatms.Utils.Log as l # Importo la clase Log
import imgatms.View.Application as a
import imgatms.View.Popup as p

# Complejos con los nombres de los ATMs
MS = ["ms-atm01", "ms-atm02", "ms-atm03", "ms-atm04",
      "ms-atm05", "ms-atm06", "ms-atm07", "ms-atm08", "ms-atm09"]
PS = ["ps-atm01", "ps-atm02", "ps-atm03", "ps-atm04"]
PC = ["pc-atm01", "pc-atm02", "pc-atm03"]
NC = ["nc-atm01", "nc-atm02", "nc-atm03"]


def start():
    print("DEBUG: Starting.")
    app = a.Application() # Creo la instancia de la aplicacion grafica
    print("DEBUG: Application closed.")

def execute(action, img_name, isCheckedMS, isCheckedPS, isCheckedPC, isCheckedNC):
    dt = d.Date()
    date = dt.getActualDatetime() # Guardo la fecha y hora actual
    log = l.Log(date)  # Creo el log con la fecha y hora actual
    print("DEBUG: Log created.")
    
    print('DEBUG: Executing.')

    #Obtengo el camino a la imagen
    img_path = os.path.join(os.getcwd(), "Img")
    img_path = os.path.join(img_path, img_name)

    log_path = os.path.join(os.getcwd(), "Log")
    log_path = os.path.join(log_path, date+'.txt')

    import imgatms.Utils.functions as f

    if isCheckedMS:
        for atm in MS:
            if action == 'cp':
                print('DEBUG: Copying to ' + atm)
                log.addLine(date+'.txt', "Copying to " + atm)
                cp_result = f.copyImg(img_name, img_path, atm, log_path)
            elif action == 'rm':
                print('DEBUG: Deleting from ' + atm)
                log.addLine(date+'.txt', "Deleting from " + atm)
                f.deleteImg(img_name, atm, log_path)
        print('')

    if isCheckedPS:
        for atm in PS:
            if action == 'cp':
                print('DEBUG: Copying to ' + atm)
                log.addLine(date+'.txt', "Copying to " + atm)
                cp_result = f.copyImg(img_name, img_path, atm, log_path)
            elif action == 'rm':
                print('DEBUG: Deleting from ' + atm)
                log.addLine(date+'.txt', "Deleting from " + atm)
                f.deleteImg(img_name, atm, log_path)
        print('')

    if isCheckedPC:
        for atm in PC:
            if action == 'cp':
                print('DEBUG: Copying to ' + atm)
                log.addLine(date+'.txt', "Copying to " + atm)
                cp_result = f.copyImg(img_name, img_path, atm, log_path)
            elif action == 'rm':
                print('DEBUG: Deleting from ' + atm)
                log.addLine(date+'.txt', "Deleting from " + atm)
                f.deleteImg(img_name, atm, log_path)
        print('')

    if isCheckedNC:
        for atm in NC:
            if action == 'cp':
                print('DEBUG: Copying to ' + atm)
                log.addLine(date+'.txt', "Copying to " + atm)
                cp_result = f.copyImg(img_name, img_path, atm, log_path)
            elif action == 'rm':
                print('DEBUG: Deleting from ' + atm)
                log.addLine(date+'.txt', "Deleting from " + atm)
                f.deleteImg(img_name, atm, log_path)
        print('')
    
    popup = p.Popup()
