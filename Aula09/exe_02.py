import os

os.system('cls')
import pandas as pd
import numpy as np


dados = pd.Series([2, 4, 6, 8, 10])

# Transforma os dados em array numpy
conjunto_dados = np.array(dados)
print(f'Conjunto de dados: {conjunto_dados}')

# Calcular a média
media = conjunto_dados.mean()
print(f'Média: {conjunto_dados.mean()}')

# Calcula a variância
variancia = np.var(conjunto_dados)
print(f'Variância da série de dados: {np.var(conjunto_dados)}')

# Calcula o devio padrão
# O desvio padrão é a raiz quadrada da variância
# print(f'Desvio Padrão da série de dados: {np.sqrt(conjunto_dados.var())}')

# Forma mais direta de calcular o desvio padrão
# Calcula diretamente o desvio padrão do conjunto de dados
desvio_padrao = np.std(conjunto_dados)
print(f'Desvio Padrão da série de dados: {np.std(conjunto_dados)}')

distancia_var_media = variancia / (media**2)
print(f'Distância entre a Variância e a média: {distancia_var_media}')

coef_variacao = (desvio_padrao / media) * 100
print(f'Coeficiente de Variação: {coef_variacao}')