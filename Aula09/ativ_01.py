import os

os.system('cls')
import pandas as pd
import numpy as np


idades = pd.Series([5, 10, 12, 35, 38])

# Transforma os dados em array numpy
conjunto_idades = np.array(idades)
print(f'Conjunto de idades: {conjunto_idades}')

# Calcular a média
media = conjunto_idades.mean()
print(f'Média: {conjunto_idades.mean()}')

# Calcula a variância
variancia = np.var(conjunto_idades)
print(f'Variância das idades: {np.var(conjunto_idades)}')

# Calcula o devio padrão
# O desvio padrão é a raiz quadrada da variância
# print(f'Desvio Padrão das idades: {np.sqrt(conjunto_idades.var())}')

# Forma mais direta de calcular o desvio padrão
# Calcula diretamente o desvio padrão do conjunto de dados
desvio_padrao = np.std(conjunto_idades)
print(f'Desvio Padrão das idades: {np.std(conjunto_idades)}')

distancia_var_media = variancia / (media**2)
print(f'Distância entre a Variância e a média: {distancia_var_media}')

coef_variacao = (desvio_padrao / media) * 100
print(f'Coeficiente de Variação: {coef_variacao}')

variancia_amostral = np.var(idades, ddof=1)
print(f'Variância Amostral: {variancia_amostral}')

desvio_padrao_amostral = np.std(idades, ddof=1)
print(f'Desvio Padrão entre idades: {desvio_padrao_amostral}')