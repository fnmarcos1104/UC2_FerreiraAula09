import os

os.system('cls')
import pandas as pd
import numpy as np


dados = {1, 2, 3, 4, 5}

# Calcula média
media = sum(dados) / len(dados)
print(f'Média: {media}')

# Calcular as diferenças entre cada valor e a média
diferencas = [x - media for x in dados]
print(f'Diferenças em relação a média: {diferencas}')

# Elevar as diferenças ao quadrado
quadrados_diferencas = [x**2 for x in diferencas]
print(f'Quadrados das diferenças: {quadrados_diferencas}')

media_quadrados_diferencas = sum(quadrados_diferencas) / len(quadrados_diferencas)
print(f'Variância é a média dos quadrados das diferenças: {media_quadrados_diferencas}')

desvio_padrao = media_quadrados_diferencas ** 0.5
print(f'Desvio padrão é a raiz quadrada da variância: {desvio_padrao}')

distancia_var_media = media_quadrados_diferencas / (media**2)
print(f'Distância entre a Variância e a média: {distancia_var_media}')

coef_variacao = (desvio_padrao / media) * 100
print(f'Coeficiente de Variação: {coef_variacao}')



conjunto_dados = np.array(dados)
print(f'Conjunto de dados: {conjunto_dados}')

variancia_amostral = np.var(dados, ddof=1)
print(f'Variância Amostral: {variancia_amostral}')

desvio_padrao_amostral = np.std(dados, ddof=1)
print(f'Desvio Padrão entre idades: {desvio_padrao_amostral}')

