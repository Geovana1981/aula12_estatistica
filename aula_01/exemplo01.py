import pandas as pd

produtos = ["Notebook", "Smartphone", "Tablet", "Smartwatch", "Câmera", "Notebook"]
qtds_estoque = [16, 28, 19, 13, 26, 9]

serie_produtos = pd.Series(produtos)
serie_quantidade = pd.Series(qtds_estoque)
print(serie_produtos)
print(serie_quantidade)
print(produtos)

# # Printando por rótulo
print(serie_produtos[1])
# # Printando por 2  ou mais rótulos
print(serie_produtos[[2, 3]])
# # Printando por 2  ou mais rótulos
print(serie_produtos[[4, 5]].values)

# Filtrando elementos
print(serie_quantidade[serie_quantidade < 20]) # Mostra somente os menores que 20
print(serie_produtos[serie_produtos == "Notebook"]) # Mostra somente os notebooks
print(serie_produtos[serie_produtos.str.startswith("Smart")]) # Mostra somente os que começam com "Smart"
print(serie_produtos[serie_produtos.str.endswith("phone")]) # Mostra somente os que terminam com "phone"
print(serie_produtos[serie_produtos.str.contains("b")]) # Mostra somente os que contêm "b"

# Operações com as series:
# Soma
serie_quantidade += 10
print(serie_quantidade) 
serie_quantidade[serie_quantidade > 30] += 25
print(serie_quantidade)

# Multiplicação
preco = [3000, 800, 2500, 600, 1990, 850]
total = serie_quantidade * preco
print(total)
