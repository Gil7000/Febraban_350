import os

for filename in os.listdir():
    if filename.endswith('.TXT'):
        with open(filename, 'r', encoding='latin-1') as arquivo:
            conteudo = arquivo.readlines()

        with open(filename+'2', 'a') as file:
            for i in range(len(conteudo)):
                linha = str(conteudo[i][0:-1])
                linha += ' '*(349-len(linha))+'.\n'
                file.write(linha)

