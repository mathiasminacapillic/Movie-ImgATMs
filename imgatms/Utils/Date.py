
import datetime

class Date:
    def getActualDatetime(self):
        """ Obtiene la fecha y hora actual """
        print("DEBUG: Obtaining actual date and time")
        d = datetime.datetime.now()
        #Quiero que todos tengan dos caracteres (excepto el anio que por defecto viene con 4 carac)
        if d.day < 10:  
            day = '0' + str(d.day)
        else:
            day = d.day

        if d.month < 10:
            month = '0' + str(d.month)
        else:
            month = d.month
        
        if d.hour < 10:
            hour = '0' + str(d.hour)
        else:
            hour = d.hour

        if d.minute < 10:
            minute = '0' + str(d.minute)
        else:
            minute = d.minute

        now = str(hour) + str(d.minute) + str(day) + str(month) + str(d.year)
        return now