from dal import Base, return_session, Cadastro, return_engine, Base
from hashlib import sha256
import os
import getpass
from controller import validar_email,enviar_email

os.system('cls')

print("""\033[1;32;40m<<CONECTAR BANCO DE DADOS>>
<DIGITE ABAIXO AS INFORMAÇÕES PARA CONECTAR AO BANCO DE DADOS>
\033[m""")


session = return_session(
    str(input("\033[1;32;40mDigite o nome do usuario: \033[m")),
    str(input("\033[1;32;40mDigite a senha: \033[m")),
    str(input('\033[1;32;40mDigite o nome do HOST: \033[m')),
    str(input("\033[1;32;40mDigite o nome do BANCO DE DADOS: \033[m")),
    int(input("\033[1;32;40mDigite a PORTA: \033[m"))
)

Cadastro()
Base.metadata.create_all(return_engine())



while True:
    
    escolha_user = int(input("""\033[36;40m
========================================    
ESCOLHA UMA DAS OPÇÕES ABAIXO:         | 
[1] CADASTRAR USUÁRIO                  |
[2] LOGAR                              |
[3] SAIR                               |
======================================== 
SUA OPÇÂO:    
    \033[m"""))
    
    match escolha_user:
        case 1:
            while True:
                try:
                    print()
                    name = str(input("\033[1;32;40mDIGITE SEU NOME: \033[m")).capitalize().strip()
                    emai = str(input("\033[1;32;40mDIGITE SEU EMAIL:  \033[m")).strip()
                    bac = session.query(Cadastro).filter_by(email=emai).all()
                    
                    
                    if (bac):
                        assert bac == True, """\033[31;40m
=========================================================
|MENSAGEM-> EMAIL INFORMADO JÁ CADASTRADO. INFORME OUTRO|
=========================================================
\033[m"""
                        continue

                    elif validar_email(emai) == False:
                        continue

                except Exception as e:
                    print(f'{e}')

                else:

                    while True:
                        senha = getpass.getpass('\033[1;32;40mDIGITE SUA SENHA:  \033[m')
                        print("""\033[33;40m
======================================================
|MENSAGEM-> Repita novamente sua senha para confirmar|
======================================================
\033[m""")
                        senha_m = getpass.getpass("\033[1;32;40mDIGITE SUA SENHA NOVAMENTE: \033[m")
                        if senha == senha_m:
                            senha = sha256(senha.encode()).hexdigest()
                            print("""\033[33;40m
===================================
|MENSAGEM-> SENHA INFORMADA VÁLIDA|
===================================
\033[m""")
                            break

                        elif senha != senha_m:
                            print("""\033[31;40m
===============================================                            
|MENSAGEM -> Senhas inseridas estão diferentes|
===============================================
\033[m""")
                            continue    
                        
                    if enviar_email(emai) == True:
                        try:
                            inserir_d = Cadastro(
                                nome=name,
                                email=emai,
                                senha=senha   
                            )

                            session.add(inserir_d)
                            session.commit()
                        except Exception as e:
                            print(f'NÃO FOI POSSÍVEL CADASTRAR DEVIDO AO ERRO >> {e}')
                        
                        else:
                            print()
                            print("""\033[32;40m
===========================
| CADASTRADO COM SUCESSO! |
===========================
\033[m""")
                        break
        case 2:
            print("""
\033[32;40m            
=======
|LOGIN|
=======
\033[m""")

            email_log = str(input("\033[32;40mDIGITE SEU EMAIL CADASTRADO: \033[m"))
            senha_log = getpass.getpass('\033[32;40mDIGITE SUA SENHA: \033[m')
            senha_log_end = sha256(senha_log.encode()).hexdigest(

            )


            verif_log = session.query(Cadastro).filter_by(email=email_log,senha=senha_log_end).all()            
            if (verif_log):
                print("""\033[32;40m
____________________

|LOGADO COM SUCESSO|
____________________
\033[m""")
                 
            else:
                print("""\033[31;40m
====================================
|MENSAGEM-> CREDENCIAIS INCORRRETAS|
====================================
\033[m""")
                verif_log = session.query(Cadastro).all()
                for x in verif_log:
                    if (x.email != email_log):
                        confirm_email = False
                    
                    elif email_log == x.email:
                        confirm_email = True
                        break

                if confirm_email == True:
                    print("""\033[31;40m
============================
|MENSAGEM-> SENHA INCORRETA|
============================
\033[m""")

                elif confirm_email == False:
                    print("""\033[31;40m
===========================================
|MENSAGEM-> EMAIL INFORMADO NÃO CADASTRADO|
===========================================
\033[m""")     

        case 3:
            print()
            print("\033[33;40m|SAINDO|\033[m")
            break
