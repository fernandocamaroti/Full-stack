produtos = []


print('1. Adicionar produto')
print('2. Deletar produto')
print('3. Atualizar produto')

op = int(input())
if op == 1:
    produto = {}
    produto['nome'] = input('Digite o nome do produto: ')
    produto['preco'] = float(input('Digite o preço do produto: '))
    produto['qtd'] = int(input('Digite a quantidade em estoque: '))
    produtos.append(produto)
    
elif op == 2:
    delete = input('Qual produto deletar?')
    for produto in produtos:
        if produto['nome'] == delete:
            produtos.remove(produto)

print(produtos)


