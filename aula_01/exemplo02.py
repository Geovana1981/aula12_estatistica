import pandas as pd

produtos = ["Notebook", "Smartphone", "Tablet", "Smartwatch", "Câmera", "Notebook"]
qtds_estoque = [16, 28, 19, 13, 26, 9]

serie_estoque = pd.Series(qtds_estoque, index=produtos)
print(serie_estoque)
print(serie_estoque["Notebook"])