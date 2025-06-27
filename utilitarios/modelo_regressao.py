"""
Aquivo com a função que faz o download dos dados e passa para um DataFrame pandas
"""

import os
from pathlib import Path

import pandas as pd

import statsmodels.api as sm
import numpy as np

from utilitarios.caminhos import tabelas_regressao # Só funciona quando executado do jupyter notebook


######################################################################

def regressao_linear(dados, X:list, y:str):
    """
    Faz regressão linear, tanto univariada quanto multivariada
    """
    nomes_X:list = X
    nome_y:str = y

    X = np.array(dados[X])
    y = np.array(dados[y])

    nome_base:str = f"{'+'.join(nomes_X)}-{nome_y}.csv"  
    
    # Criando modelo:
    X = sm.add_constant(X)

    modelo = sm.OLS(y, X).fit()

    # Salvando modelo em tabela:
    tabela = modelo.summary2().tables[1]
    tabela.to_csv(Path(tabelas_regressao, nome_base))

    return modelo

def predicao_regressao(dados, modelo, X:list) -> list:
    """
    Faz a predição de acordo com o modelo ajustado
    """
    X = np.array(dados[X])
    X = sm.add_constant(X)

    return modelo.predict(X)
    
