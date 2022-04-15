def b_xml(direction,log_name,csv_name,today_aux):

    log_file = open(log_name, 'a')
    log_file.write('B - XML \n')
    print('B - XML')
    log_file.close()

    # Importo el modulo con el envio de mail
    from A_Email_error import enviar_mail_error
    import requests
    # Liberia para salir del flujo
    import sys
    from bs4 import BeautifulSoup

    # URL del servicio a obtener
    URL = ""

    try:
        r = requests.get(URL, timeout = 600)
        r.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print("Http Error:" + str(errh))
        log_file = open(log_name, 'a')
        log_name.write("Http Error:" + str(errh)+"\n")
        log_name.write('-------------------------------------\n')
        log_name.close()
        enviar_mail_error(log_name)
        sys.exit()
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:" + str(errc))
        log_file = open(log_name, 'a')
        log_file.write("Error Connecting:" + str(errc)+'\n')
        log_file.write('-------------------------------------\n')
        log_file.close()
        enviar_mail_error(log_name)
        sys.exit()
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:" + str(errt))
        log_file = open(log_name, 'a')
        log_file.write("Timeout Error:" + str(errt)+'\n')
        log_file.write('-------------------------------------\n')
        log_file.close()
        enviar_mail_error(log_name)
        sys.exit()
    except requests.exceptions.RequestException as err:
        print("OOps: Something Else" + str(err))
        log_file = open(log_name, 'a')
        log_file.write("OOps: Something Else" + str(err)+'\n')
        log_file.write('-------------------------------------\n')
        log_file.close()
        enviar_mail_error(log_name)
        sys.exit()

    string_xml = r.content
    # parser = ET.XMLParser(encoding="ISO-8859-1")
    # parser = ET.XMLParser(encoding="utf-8")
    # parser = ET.XMLParser(encoding="utf-16")
    # tree = ET.fromstring(r.content, parser)
    # print(tree.findall('<nombre>'))

    soup = BeautifulSoup(string_xml, 'xml')

    lista_prod = list()
    lista_prod.append("\'"+
                      "id"+"\'"+","+
                      "\'"+"title"+"\'"+","+
                      "\'"+"description"+"\'"+","+
                      "\'"+"link"+"\'"+","+
                      "\'"+"availability"+"\'"+","+
                      "\'"+"price"+"\'"+","+
                      "\'"+"currency"+"\'"+","+
                      "\'"+"brand"+"\'"+","+
                      "\'"+"adult"+"\'"+","+
                      "\'"+"product_type"+"\'"+","+
                      "\'"+"condition"+"\'"+","+
                      "\'"+"tiem_dia_id"+"\'"+","+
                      "\'"+"model"+"\'"+","+
                      "\'"+"product_type1"+"\'"+","+
                      "\'"+"product_type2"+"\'"
                      +"\n")

    for cod_bar in soup.findAll('item'):
        lista_prod.append(
            "\'"+
            cod_bar.find('g:id').text+
            "\'"+','+
            "\'"+
            cod_bar.find('g:title').text+
            "\'"+','+
            "\'"+
            cod_bar.find('g:description').text+
            "\'"+','+
            "\'"+
            cod_bar.find('g:link').text+
            "\'"+','+
            "\'"+
            cod_bar.find('g:availability').text+
            "\'"+','+
            "\'"+
            cod_bar.find('g:price').text[0:-3]+
            "\'"+','+
            "\'"+
            cod_bar.find('g:price').text[-3:]+
            "\'"+','+
            "\'"+
            cod_bar.find('g:brand').text+
            "\'"+','+
            "\'"+
            cod_bar.find('g:adult').text+
            "\'"+','+
            "\'"+cod_bar.find('g:product_type').text+
            "\'"+','+
            "\'"+cod_bar.find('g:condition').text+
            "\'"','+
            "\'"+today_aux+ # TIEM_DIA_ID
            "\'"','+
            "\'"+ # MODELO
            "\'"','+
            "\'"+ # PRODUCT_TYPE1
            "\'"','+
            "\'"+ # PRODUCT_TYPE2
            "\'"
            +"\n"
            )

    # Guardo los productos en un csv
    file = open(csv_name, 'w+', newline ='',encoding="utf-8")
    for linea in lista_prod:
        file.write(linea)
    file.close()

    return lista_prod
