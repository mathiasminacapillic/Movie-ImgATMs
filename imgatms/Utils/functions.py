
import os
import os.path

#Functions
def pushDirectory(atm_name):
    os.system('pushd \\\\'+atm_name+'\\VISTA')

def popDirectory(atm_name):
    os.system('popd')

def copyImg(img_name, img_path, atm_name, log_path):
    #Obtengo el camino al archivo a ejecutar
    exe = os.path.join(os.getcwd(), "imgatms")
    exe = os.path.join(exe, "src")
    exe = os.path.join(exe, "cmd")
    exe = os.path.join(exe, "copyimg.cmd")

    #os.system escribe en la consola para ejecutar el cmd con los parametros que requiere
    pushDirectory(atm_name)
    os.system(exe+' '+img_name+' '+img_path+' '+atm_name+' '+log_path)
    popDirectory(atm_name)

def deleteImg(img_name, atm_name, log_path):
    #Obtengo el camino al archivo a ejecutar
    exe = os.path.join(os.getcwd(), "imgatms")
    exe = os.path.join(exe, "src")
    exe = os.path.join(exe, "cmd")
    exe = os.path.join(exe, "deleteimg.cmd")

    #Ejecucion
    os.system(exe+' '+img_name+' '+atm_name+' '+log_path)