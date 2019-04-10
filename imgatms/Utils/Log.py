import os.path

class Log:
    def __init__(self, date):
        """ Crea el archivo con nombre de la fecha actual en el directorio Log """
        print("DEBUG: Creating log file.")
        p = "Log"
        if os.path.exists(p):
            d_name = str(date) + '.txt'
            f_name = os.path.join(p, d_name)
            f = open(f_name, "x")
            print('DEBUG: Log created')
            f.close()
        else:
            print("DEBUG: ERROR: The directory does not exists!")
    
    def addLine(self, log_name, text):
        """ Agrega una linea (el texto 'text') en el archivo con nombre 'log_name' """
        print("DEBUG: Adding a line to log file")
        p = "Log"
        if os.path.exists(p):
            f_name = os.path.join(p, log_name)
            f = open(f_name, "a")
            f.write(text + '\n')
            print("DEBUG: Line added")
            f.close()
        else:
            print("DEBUG: ERROR: The directory does not exists!")
