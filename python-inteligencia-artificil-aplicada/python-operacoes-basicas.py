"""
    Explorando Células, a Função print e Tipo de dados.
"""

hello_world = "Olá Mundo"

print(hello_world)
print("\n",hello_world)
print(f"\n{hello_world}" + ", Ramon")
print()

"""
    Variáveis, Operações Matemáticas e Concatenação de Strings. 
"""

soma = 5 + 2
print(soma)
print(5 + 3)
print()


produto = 200000
print(produto)
print()

soma2 = produto + soma
print(soma2)
print(produto + soma)
print()

nome_produto1 = "Macarrão"
nome_produto2 = "Celular"
nome_produto3 = "Bala"

print(nome_produto1 + nome_produto2 + nome_produto3)
print(nome_produto1 + ", " + nome_produto2 + ", " + nome_produto3)

"""
    Operações Matemáticas e Variáveis em Python
"""

aluguel = 1000
supermercado = 2500
carro = 800

total = aluguel + supermercado + carro

print()
print(total)
print(aluguel + supermercado + carro)

aluguel = 900
total = aluguel + supermercado + carro
print(total)
print(aluguel + supermercado + carro)

aluguel = aluguel - 100
print(aluguel)
aluguel += 100
aluguel -= 100

print(aluguel)

novo_aluguel = aluguel * 2
print(novo_aluguel)

amigos = 5
total_por_pessoal = total / amigos
print(total / amigos)
print(total_por_pessoal)

"""
    Nomeclatura e tipos de dados em Python 'int', 'flaot', 'str' e 'bool'
"""

name_complete = "Ramon Rodrigues Valeriano"
print(type(name_complete))

idade = 36
casado = True
altura = 1.70

print(type(idade))
print(type(casado))
print(type(altura))

"""
    Manipulando Strings em Python: Métodos `lower`, `upper`, `strip`, `split` e `replace`
"""

complete_text_start = " Ramon   Rodrigues Valeriano "
print(complete_text_start)

upper_text_complete = complete_text_start.upper()
print(upper_text_complete)

lower_text_complete = complete_text_start.lower()
print(lower_text_complete)

split_text_complet = complete_text_start.split(" ")
print(split_text_complet)

split_text_complet = complete_text_start.split()
print(split_text_complet)

filhos = "Gael,Dante,Rayan"
print(filhos)
splint_filhos = filhos.split(",")
print(splint_filhos)

espacos_externos = complete_text_start.strip()
print(espacos_externos)

replace_text = complete_text_start.replace("  ", " ").strip()
print(replace_text)

