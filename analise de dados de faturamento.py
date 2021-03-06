# -*- coding: utf-8 -*-
"""PREDIÇÃO DE FATURAMENTO.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/112MTj6FgbH6l20WnUBjHeC22hxu-4ze-

# MÉTODO PARA PREDIÇÃO DE VENDAS/FATURAMENTO
"""

pip install statsmodels --upgrade

import numpy as np
import pandas as pd

"""Importar as bibliotecas NUMPY E PANDAS """

#IMPORTAR AS BIBLIOTECAS NUMPY E PANDAS

from google.colab import drive

drive.mount('/content/gdrive')

df = pd.read_csv('/content/df.csv').round(2)
df.columns = ['Ano', 'Mes', 'Faturamento']
df.head()

"""Análise do DataSet
 Em todo trabalho que envolve dados deve-se criar o costume de observar como os dados se comportam dentro afim de tirar alguns inseghts prévios ou até mesmo fazer a verificação se há algum problema antes de começar a devida predição para que deste modo   se puder realizar o tratamento de qualquer problema antes mesmo de se começar com a predição dos dados esta  atitude evita erros provenientes dos dados e não de nossa lógica.

 
"""

df.info()

df['Mes'].unique()

#Método prático com FOR
meses = df['Mes'].unique()
i = 1 #variavel auxiliar

#itera sobre a lista contendo os meses substituindo um por por pelo número correspondente 

for mes in meses:
  df.loc[df['Mes'] == mes, 'Mes'] = i
  i = i + 1

df.head()

#CÁLCULO DA MÉDIA ARITMÉTICA
 #ATRAVÉS DA FORMÚLA:


media = df['Faturamento'].mean()
print('Nós proximos meses sera faturado R$', media, 'mes em média')

"""No entanto podemos melhorar a nosssa resposta calculando o desvio padrão """

devpad = df['Faturamento'].std()
print('O faturamento para os proximos meses sera de R$' ,media, '/mes em media podendo variar R$', devpad, 'para mais ou para menos')

colunas = ['Min', 'Média', 'Max', ]
min = media - devpad
max = media + devpad
valores = np.array([min, media, max])

df_media = pd.DataFrame([valores] , columns = colunas).round(2)
df_media

coe_var = (devpad / media) * 100

print('O faturamento em torno de: ', coe_var, '%')

"""E para ajudar pode-se interpretar como;
1º Até 10%  é uma variação otima !!
2º De 10% á 20%; Bom
3º Entre 20% a 30%; Regular
4º Entre 30% á 40%; Ruim(Muita variação).
"""

import matplotlib.pyplot

matplotlib.pyplot.plot(df['Faturamento'], marker='o')

"""Por curiosidade podemos fazer a descrição do modo a ter o entendimento sobre  as metricas de cada valor."""

df.describe().round(2)

import seaborn as sns

#Grafico do ano de 2018

df2018 = df.loc[df['Ano'] == 2018]
sns.jointplot(data = df2018, x="Mes", y="Faturamento")

#Grafico do ano de 2019

df2018 = df.loc[df['Ano'] == 2019]
sns.jointplot(data = df2018, x="Mes", y="Faturamento", color = 'brown')

#Grafico do ano de 2020

df2018 = df.loc[df['Ano'] == 2020]
sns.jointplot(data = df2018, x="Mes", y="Faturamento", color = 'black')

"""ANALISE POR REGRESSÃO LINEAR"""

ax = sns.regplot(x = df.index, y="Faturamento", data=df)

"""SÉRIES TEMPORAIS"""



