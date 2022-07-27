
import re
import smtplib
import email.message
import random


def enviar_email(email_user):  
    print("""\033[33;40m
===============================================================================
|MENSAGEM-> FOI ENVIADO UM CÓDIGO PARA SEU EMAIL PARA CONFIRMAR O SEU CADASTRO|
===============================================================================
\033[m""")

    #Gerador Código
    lista_num = [1,2,3,4,5,6,7,8,9]
    cod_gerado = random.choices(lista_num,k=4)
    cod_formato = ''
    for x in cod_gerado:
        cod_formato += f'{x}'


    corpo_email = f"""
    <p> CÓDIGO: {cod_formato}  </p>
    <p></p>
    """

    msg = email.message.Message()
    msg['Subject'] = "CONFIRMAR CADASTRO"
    msg['From'] = 'testeparaprojetos321@gmail.com'
    msg['To'] = email_user
    password = 'rnpbvfudamjpbjft' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print("""\033[33;40m
==========================
|MENSAGEM-> Email enviado|
==========================
\033[m""")
    while True:
        digite_cod = str(input("""\033[32;40mDigite o código para confirmar o cadastro: \033[m"""))

        if digite_cod == cod_formato:
            print("""\033[32;40m
=================
|CÓDIGO VALIDADO|
=================
\033[m""")
            break

        else:
            print("""\033[31;40m
=================
|CÓDIGO INVALIDO|
=================
\033[m""")
            continue
    return True






def validar_email(email_user):
    pattern = '^[a-z 0-9]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$'
    
    if re.search(pattern, email_user):
        print("""\033[33;40m
===================================
|MENSAGEM-> EMAIL INFORMADO VÁLIDO|
===================================
\033[m""")
        return True
    
    else:
        print(f"""\033[31;40m
=====================================
|MENSAGEM-> EMAIL INFORMADO INVÁLIDO|        
=====================================
\033[m
""")
        return False





