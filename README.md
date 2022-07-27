# Projeto_LOGIN_PYTHON
Projeto Login Python com SQL ALCHEMY

PYTHON
ORM = SQL ALCHEMY

Funcionalidades:
  *Cadastrar Usuário:
    >Validar email.
    >EMAIL E SENHA
        !Utilizei o GETPASS para esconder os caracteres da senha(acredito que deixa mais seguro)
        !A senha quando vai registrar/logar ela é transformada em um hash(sha256)
    >Enviar um código gerado p email informado para confirmar o cadastro.
    >Caso já exista o email no banco ele irá retornar uma mensagem de AVISO.
 
  *Logar Usuário:
    >Caso coloque um email que não exista no BD ele irá retornar uma mensagem de ERRO.
    >Caso coloque o email que tenha no BD, mas se colocar a senha errada irá retornar uma mensagem de ERRO.
