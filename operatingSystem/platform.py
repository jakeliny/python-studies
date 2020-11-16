import platform

#retorna a ditribuição exata do SO ou que esta sendo executada
print("Distribuição do Sistema Operacional.: ", platform.platform())

#retorna o nome do SO
print("Nome do Sistema Operacional.........: ", platform.system())

#retorna a versão do SO
print("Versão do Sistema Operacional.......: ", platform.release())

#retorna a arquitetura da maquina
print("Arquitetura.........................: ", platform.architecture())

#retorna o nome do computador na rede
print("Nome do Computador..................: ", platform.node())

#retorna a arquitetura do processador
print("Tipo de Máquina.....................: ", platform.machine())
print("Processador.........................: ", platform.processor())

#retorna a versão do python
print("Versão do Python....................: ", platform.python_version())