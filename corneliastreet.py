#usando a função open para criar um objeto do tipo arquivo
arquivo = open("C:\\Users\\reali\\Desktop\\arquivo_texto.txt", 'r')

#printando o conteúdo do objeto do arquivo
print(arquivo.read(50))

print(arquivo.readline())

for linha in arquivo.readlines():
    print(linha, end='')

linhas_do_arquivo = arquivo.readlines()
linhas_do_arquivo.sort()
print(linhas_do_arquivo)

#recuperando uma linha do arquivo
linha = arquivo.readline()
palavras = linha.split()

#printando as palavras de uma linha usando split()
print(palavras)

#printando uma linha do arquivo
print(arquivo.readline())
print(arquivo.readline())

#descobrindo onde está o controle do arquivo
print("Atualmente o arquivo está em:", arquivo.tell())

#voltando para a primeira linha
arquivo.seek(0)
print("Agora o arquivo está em:", arquivo.tell())

#printando a primeira linha do arquivo
print(arquivo.readline())
arquivo.close()

#alterar o arquivo para write 
conteudo = "Estou testando criar um arquivo de texto"
arquivo = open("C:\\Users\\reali\\Desktop\\arquivo_texto.txt", 'w')
arquivo.write(conteudo)

arquivo.close()

#alterar 'w' para 'a' para acrescentar conteudo no mesmo arquivo




import csv

with open('jedis.csv') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv, delimiter=',', quotechar='"')
    next(leitor_csv)  # Ignora a primeira linha, que contém apenas os títulos das colunas
    for linha in leitor_csv:
        mensagem = f"O Jedi de nome {linha[0]}, com {linha[1]} anos de idade, é classificado como {linha[2]}."
        print(mensagem)
        
#write no csv
import csv

dados_jedi = ['Yoda', '900', 'Mestre']

with open('jedis.csv', mode='a', newline='') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv, delimiter=',')
        escritor_csv.writerow(dados_jedi)

#se fosse 2 jedis
import csv

dados_jedi = [['Yoda', '900', 'Mestre'], ['Luke Skywalker', '23', 'Padawan']]

with open('jedis.csv', 'a', newline='') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv, delimiter=',')
    for linha in dados_jedi:
        escritor_csv.writerow(linha)

print('Dados adicionados com sucesso!')




#JSON
#importando o módulo json
import json

#criando um dicionário para usarmos como exemplo
contatos = {
    "Clark Kent":
        {"Celular":"123456",
         "Email":"super@krypton.com"},
    "Bruce Wayne":
        {"Celular":"654321",
         "Email":"bat@caverna.com.br"}
}

#convertendo o dicionário para uma string o formato json
final = json.dumps(contatos)

#exibindo a string convertida
print(final)

#indent espaçamento dos dados
#importando o módulo json
import json

#criando um dicionário para usarmos como exemplo
contatos = {
    "Clark Kent":
        {"Celular":"123456",
         "Email":"super@krypton.com"},
    "Bruce Wayne":
        {"Celular":"654321",
         "Email":"bat@caverna.com.br"}
}

#convertendo o dicionário para uma string o formato json
final = json.dumps(contatos, indent=4)

#exibindo a string convertida
print(final)







#write no JSON

#importando o módulo json
import json

#criando um dicionário para usarmos como exemplo
contatos = {
    "Clark Kent":
        {"Celular":"123456",
         "Email":"super@krypton.com"},
    "Bruce Wayne":
        {"Celular":"654321",
         "Email":"bat@caverna.com.br"}
}

#convertendo o dicionário para uma string o formato json
final = json.dumps(contatos, indent=4)

#criando um arquivo
arquivo = open("c:\arquivos\agenda.json", "w")

#escrevendo o JSON dentro do arquivo
arquivo.write(final)

#fechando o arquivo
arquivo.close()






#Abrindo um arquivo JSON e convertendo para um dicionário
import json
#Criando uma variável de texto
conteudo = "Estou testando criar um arquivo de texto. Então, estou... textando?"

#usando a função open para criar um objeto do tipo arquivo
arquivo = open("c:\arquivos\agenda.json")

#colocando o conteúdo do arquivo em uma variável do tipo string
conteudo_do_arquivo = arquivo.read()

#fechando o arquivo
arquivo.close()

#usando o método loads para converter uma string no formato json em um dicionário
agenda = json.loads(conteudo_do_arquivo)

#comprovando que o objeto agenda é do tipo dicionário
print("O tipo do objeto agenda é {}".format(type(agenda)))