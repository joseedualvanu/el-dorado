def c_transformacion(direction,log_name,csv_name):
    import datetime

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

    log_name = direction + 'Logs/Registro_' + str(today) + '.log'
    csv_name = direction + 'Precios/Precios_' + str(today) + '.csv'

    log_file = open(log_name, 'a')
    log_file.write('C - Transformation\n')
    print('C - Transformation')
    log_file.close()

    import pandas as pd
    # from A_Email_error import enviar_mail_error

    # Test with panda dataframe
    lista = pd.read_csv(csv_name,delimiter=',',quotechar='\'',index_col=False)

    for ind in lista.index:
        if  "Modelo" in lista['description'][ind]:
            line1 = lista['description'][ind].split("Modelo")
            # index = line1.index("Modelo")
            line1_aux = str(line1[1]).strip()
            lista['model'][ind] = line1_aux

            # print(lista[1][ind]+'-----------'+model)

        line2 = lista['product_type'][ind].split(">")
        lista['product_type1'][ind] = line2[0]
        if len(line2) == 2:
            lista['product_type2'][ind] = line2[1]

    return lista
