#criando lista de nomes das armaduras
nomes_armadura = ['Mark IV', 'Mark II', 'Mark III']
print("Lista inicial de armaduras:", nomes_armadura)

#adicionando nova armadura no final da lista utilizando append
nova_armadura = (input("Digite o nome da nova armadura: "))
nomes_armadura.append(nova_armadura)
print("Lista de armaduras atualizada: ", nomes_armadura)

#adicionando uma armadura em um índice específico da lista
#mostrando as posições disponíveis na lista
print(f'Posições disponíveis: de 0 a {len(nomes_armadura)}')
nova_armadura = input("Digite o nome da nova armadura: ")

#solicitando uma posição até que seja fornecida uma posição válida
while True: 
    posicao = int(input("Digite a posição onde a nova armadura será inserida: "))
    if posicao >= 0 and posicao <= len(nomes_armadura):
        break
    print(f'Posição inválida. Digite uma posição entre 0 e {len(nomes_armadura)}')

nomes_armadura.insert(posicao, nova_armadura)
print("Lista de armaduras atualizadas:", nomes_armadura)

#ordenando as listas em ordem alfabética utilizando o sort()
print("Lista de armaduras desordenadas:", nomes_armadura)
nomes_armadura.sort()
print("Lista de armaduras ordenadas:", nomes_armadura)

#reverse=true para ordenar em decrescente
nomes_armadura.sort(reverse=True)
print("Lista de armaduras em ordem decrescente:", nomes_armadura)

# a função sort() pode receber o argumento key=str.lower para ignorar maiusculas e minusculas
nomes_armadura.sort(key=str.lower)
print("Lista de armaduras ordenadas ignorando maiusculas e minusculas", nomes_armadura)

# selecionando um intervalo de elementos usando slicing
inicio = int(input("Digite a posicao inicial do intervalo: "))
fim = int(input("Digite a posicao final do intervalo: "))
intervalo = nomes_armadura[inicio:fim]
print("INtervalo de armaduras selecionado:", intervalo)

#criando tuplas de caracteristicas das armaduras
print("Digite as caracteristicas da nova armadura:")
caracteristicas_armadura = {
    ('Ferro', 'Pequena', 200),
    ('Titanio', 'Media', 300),
    ('Liga Metalica', 'Grande', 500),
    (input("Digite o material da nova armadura: "), input("Digite o tamanho da nova armadura:"), input("Digite o peso da nova armadura:"))
}
print("Caracteristicas das armaduras:", caracteristicas_armadura)

#contando a quantidade de elementos na tupla usando o len()
qtde_caracteristicas = len(caracteristicas_armadura)
print(qtde_caracteristicas)

#contando a quantidade de elementos repetidos na tupla
material = input("Digite o material que deseja contar: ")
quantidade = 0
for i in range(qtde_caracteristicas):
    if caracteristicas_armadura[i][0] == material:
        quantidade += 1
print("Quantidade de armaduras com o material", material, ':', quantidade)

#Criando o dicionário de informações detalhadas das armaduras
informacoes_armaduras = {
    "Mark I": {"ano": 2008, "proteçao":"baixa", "potencia de fogo:": 10},
    "Mark II": {"ano": 2018, "proteçao":"media", "potencia de fogo:": 20},
    "Mark III": {"ano": 2004, "proteçao":"alta", "potencia de fogo:": 30},
    "Mark IV": {"ano": 2002, "proteçao":"alta", "potencia de fogo:": 50},
}

#obtendo a lista de tuplas(chave, valor) do dicionario usando o método items()
lista_tuplas = informacoes_armaduras.items()
print("Lista de tuplas do dicionario de informações das armaduras:", lista_tuplas)

#atualizando informações de uma armadura no dicionario utilizando update()
print("Armaduras disponiveis:", list(informacoes_armaduras.keys()))
armadura = input("Digite o nome da nova armadura que deseja atualizar: ")
ano = int(input("Digite o ano de lancamento da armadura: "))
protecao = input("Digite o nível de proteção da armadura: ")
potencia = int(input("Digite a potencia de fogo da armadura: "))

informacoes_armaduras.update({armadura: {'ano': ano, 'protecao': protecao, 'potencia de fogo': potencia}})
print("Informações da armadura", armadura, "atualizadas:", informacoes_armaduras[armadura])

#removendo uma armadura do dicionário usando pop()
armadura = input("Digite o nome da armadura que deseja remover" + str(list(informacoes_armaduras.keys())) + ': ')
informacoes_armaduras.pop(armadura)
print('Armadura', armadura, 'removida do dicionario.')

#apresentando dicionario inteiro
for chave, valor in informacoes_armaduras.items():
    print('Nome:', chave)
    print('Ano de lançamento:', valor["ano"])
    print('Nivel de proteção:', valor["proteçao"])
    print('Potencia de fogo:', valor["potencia de fogo:"])
    print('') #linha em branco para separar as informações de cada armadura