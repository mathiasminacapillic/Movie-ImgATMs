:: El orden de los parametros es:
:: %1 - img_name
:: %2 - img_path
:: %3 - atm_name: complejo-atmXX (Ej. ms-atm01)
:: %4 - log_path

@echo off

::Verifica que se reciban 4 y solo 4 parametros
if {%1}=={} goto error
if {%2}=={} goto error
if {%3}=={} goto error
if {%4}=={} goto error
if {%5} NEQ {} goto error

pushd \\%3\VISTA

::Verifica que exista la imagen, que existan los directorios
::y que no exista la img a donde la queremos copiar
if not exist %2 goto error1
if not exist Z:\VistaKiosk\Config\Video goto error2
if exist Z:\VistaKiosk\Config\Video\%1 goto aviso

::Proceso de copiado
copy %2 Z:\VistaKiosk\Config\Video\
if not errorlevel 1 goto correcto

echo Copia errónea. Verifique permisos de la carpeta destino. >> %4
goto :fin

:error
echo Error. Deben recibirse 4 y solo 4 parametros >> %4
goto :fin

:error1
echo Imagen origen no existe. >> %4
goto :fin

:error2
echo Carpeta destino no existe. >> %4
goto :fin

:aviso
echo El archivo ya existe en el destino. No se ha realizado copia. >> %4
goto :fin

:correcto
echo Archivo copiado correctamente. >> %4
goto :fin

:fin
popd