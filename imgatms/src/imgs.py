#!/usr/bin/env python
#
"""
Orden de los parámetros:
sys.argv[1] = img_name
"""

import sys
import os
import os.path
import time
import datetime

# Own librarys
import functions as f
from Log import *

log = Log()

# img_name = "Movie-oscars18-protectorATM968x697.jpg"
img_name = sys.argv[1]
action = sys.argv[2]

executeMS = sys.argv[3]
executePS = sys.argv[4]
executePC = sys.argv[5]
executeNC = sys.argv[6]
if executeMS == 'True':
    print("Check en MS")
if executePS == 'True':
    print("Check en PS")
if executePC == 'True':
    print("Check en PC")
if executeNC == 'True':
    print("Check en NC")

    # Ver la accion y obtener la ruta al archivo
    if action == 'cp':
        actiontxt = 'Copiar a'
        img_path = os.path.join(os.getcwd(), "src")
        img_path = os.path.join(img_path, "img")
        img_path = os.path.join(img_path, img_name)
    elif action == 'rm':
        actiontxt = 'Eliminar de'

    

# Fin del if action != '3'
# Fin del do while
os.system('cls')
