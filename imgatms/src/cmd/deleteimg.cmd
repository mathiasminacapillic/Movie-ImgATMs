:: El orden de los parametros es:
:: %1 - img_name
:: %2 - atm_name
:: %3 - log_path

@echo off

::Verifica que se reciba 1 y solo 1 parametro
if {%1}=={} goto error
if {%2}=={} goto error
if {%3}=={} goto error
if {%4} NEQ {} goto error

pushd \\%2\VISTA

::Verifica que exista la imagen, que existan los directorios
::y que no exista la img a donde la queremos copiar
if not exist Z:\VistaKiosk\Config\Video\%1 goto error1
if not exist Z:\VistaKiosk\Config\Video\deleted goto error2
::if exist Z:\VistaKiosk\Config\Video\deleted\%1 goto aviso

::Ejecucion del comando
move Z:\VistaKiosk\Config\Video\%1 Z:\VistaKiosk\Config\Video\deleted
if not errorlevel 1 goto correcto

echo Error al mover. Verifique permisos de la carpeta destino. >> %3
goto :fin

:error
echo Error. Deben recibirse tres y solo tres parametros. >> %3
goto :fin

:error1
echo Imagen no existe en el directorio. >> %3
goto :fin

:error2
echo Carpeta destino no existe. >> %3
goto :fin

:aviso
echo El archivo ya existe en el destino. No se ha realizado copia. >> %3
goto :fin

:correcto
echo El archivo se ha movido correctamente. >> %3
goto :fin

:fin
popd