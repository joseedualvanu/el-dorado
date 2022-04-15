"""
MODULO A
    Description: main module, run other modules

    Args:
		--
    Returns:

    Error:
        --
    Note:
        See https://www.datacamp.com/community/tutorials/docstrings-python
"""

# Library for logging
# log levels: debug(lowest), info, warning, error, critical(highest)
import logging
import datetime
import os

# import for sending mail ok
from A_Email_ok import enviar_mail_ok

# Get actual date and hour
start_time = datetime.datetime.now()
day = start_time.day
month = start_time.month
year = start_time.year
hour = start_time.hour
minute = start_time.minute
second = start_time.second

today = str(day)+str(month)+str(year)
today_aux = str(year)+'-'+str(month)+'-'+str(day)
hour_aux = str(hour)+':'+str(minute)+':'+str(second)
direction = os.path.dirname(os.path.abspath(__file__))+'/'

# private key direction
file_keyP8 = ''

logging.basicConfig(filename= direction + 'ElDorado.log',level=logging.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s')
# logging.disable(logging.debug)
logging.debug('Start of program')


log_name = direction + 'Logs/Registro_' + str(today) + '.log'
csv_name = direction + 'Precios/Precios_' + str(today) + '.csv'
# Log the beginning
log_file = open(log_name, 'a')
log_file.write('-------------------------------------\n')
log_file.write('Script ElDorado Alert\n')
log_file.write('Comienzo\t'+ str(hour_aux)+'\n')
log_file.close()
# Print to save the log
print('-------------------------------------')
print('Script - ElDorado')
print('Comienzo\t'+ str(hour_aux))

from B_XML import b_xml
lista_prod = b_xml(direction,log_name,csv_name,today_aux)

from C_Transformacion import c_transformacion
lista = c_transformacion(direction,log_name,csv_name)

from D_Snow import d_snow
sql = d_snow(direction,log_name,csv_name,lista,file_keyP8)

# Get date and hour for the end
start_time = datetime.datetime.now()
hour_aux = start_time.hour
minute = start_time.minute
second = start_time.second

hour = str(hour_aux)+':'+str(minute)+':'+str(second)
print('Fin\t\t\t'+ str(hour))
print('-------------------------------------')
# Registro el final
log_file = open(log_name, 'a')
log_file.write('Fin\t\t\t'+ str(hour)+'\n')
log_file.write('-------------------------------------\n')
log_file.close()

logging.debug('End of program')

# Notificacion por mail OK
# enviar_mail_ok(log_name)
