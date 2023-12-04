# Trabalho final - Redes


## Pré-requisitos

Ter o Python instalado em seu sistema. Este projeto foi desenvolvido e testado usando Python 3.

Para usar o Python via terminal adicionar ao Path nas váriaveis de ambiente (Windows).


## Alterar os IPs 

Nos arquivos fontes server.py e client.py, adicione o IP do host e uma porta livre. Para verificar as portas livres utilize netstat -a (windows) ou apenas netstat (linux), e para verificar o ip utilize o ipconfig (windows) ou ifconfig (linux).

## Executando o Servidor

No diretório do projeto, execute o servidor:

    python server.py
    

## Executando o Cliente

 Em um novo terminal, execute o cliente:

    python client.py

    O cliente tentará se conectar ao servidor e fazer solicitações HTTP.
