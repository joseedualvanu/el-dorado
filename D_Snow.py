
def d_snow(direction,log_name,csv_name,lista,file_keyP8):

    log_file = open(log_name, 'a')
    log_file.write('D - Snowflake\n')
    print('D - Snowflake')
    log_file.close()

    from snowflake import connector
    import sys
    from A_Email_error import enviar_mail_error

    import pandas as pd
    import snowflake.connector
    from snowflake.sqlalchemy import URL
    from sqlalchemy import create_engine

    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives.asymmetric import rsa
    from cryptography.hazmat.primitives.asymmetric import dsa
    from cryptography.hazmat.primitives import serialization

    with open(file_keyP8, "rb") as key:
        p_key= serialization.load_pem_private_key(
            key.read(),
            password=None,
            backend=default_backend()
        )

    pkb = p_key.private_bytes(
        encoding=serialization.Encoding.DER,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption())
    # Fill in your SFlake details here

    engine = create_engine(URL(
        user='',
        account='',
        warehouse='',
        database='',
        schema=''),
        connect_args={'private_key': pkb,}
        )

    connection = engine.connect()

    lista.to_sql('FT_PRECIOS_ELDORADO', con=engine, index=False,if_exists='append') #make sure index is False, Snowflake doesnt accept indexes

    connection.close()
    engine.dispose()
