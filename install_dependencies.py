import subprocess

# Ler o arquivo requirements.txt e extrair as linhas
with open('requirements.txt', 'r') as file:
    requirements = file.readlines()

# Remover espaços em branco e quebras de linha de cada linha
requirements = [req.strip() for req in requirements]

# Instalar cada biblioteca listada no arquivo requirements.txt
for req in requirements:
    subprocess.run(['pip', 'install', req])
