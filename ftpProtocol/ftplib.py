from ftplib import *

# Variavel para definir se a conexão sera ativa ou passiva
ftp_ativo=False

#cria o acesso ao endereço ftp
ftp = FTP('ftp.debian.org')

#retorna uma mensagem padrão pelo servidor
print(ftp.getwelcome())


usuario=input("Digite o usuario: ")
senha=input("Digite a senha: ")

#realizanod login com usuario e senha
ftp.login(usuario, senha)

#pwd retorna o diretorio atual
print("Diretório atual de trabalho: ", ftp.pwd())

#cwd altera o diretorio
ftp.cwd('doc')
print("Diretório corrente: ", ftp.pwd())

#lista os arquivos e pastas do diretorio
print(ftp.retrlines('LIST'))

#fecha a conexão FTP
ftp.quit()