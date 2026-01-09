import pandas  as pd

produtos = ["Notebook", "Smartphone", "Tablet", "Smartwatch", "Câmera", "Notebook"]
qtds_estoque = [16, 28, 19, 13, 26, 9]

serie_estoque = pd.Series(qtds_estoque, index=produtos)
print(serie_estoque)
print(serie_estoque["Notebook"])
print(serie_estoque["Notebook", "Tablet"])
print(serie_estoque[["Notebook", "Tablet"]].values)

# Filtrar
print(serie_estoque[serie_estoque < 20])
print(serie_estoque[serie_estoque.index.str.startswith ("Smart")])

# Acrescentar 5 em todas as entradas
serie_estoque += 5
print(serie_estoque)

# Acrescentando um novo produto
serie_estoque["Headphone"] = None
print(serie_estoque)

# Cria a série preço
preco =pd.Series([3500, 2500, 1200, 1000, 2600], index=produtos)

# Multiplicação
serie_total_produtos = preco * serie_estoque
print(serie_total_produtos)