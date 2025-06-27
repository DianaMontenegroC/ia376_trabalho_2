"""
Aquivo com a funções que normalizam ou transforma dados
"""

import os
from pathlib import Path

import pandas as pd

def normalizacao(dados:"DataFrame", media:dict, desvio_padrao:dict) -> "DataFrame":
    """
    Aplica normalização usando média e variância, recebe um DataFrame Pandas
    """
    novo_dado = dados.copy()
    for coluna in dados.columns:
        novo_dado[coluna] = (dados[coluna] - media[coluna]) * 1/desvio_padrao[coluna]

    return novo_dado

def desnormalizar(dados:"numpy", media:float, desvio_padrao:float) -> "Dataframe":
    """
    Aplica caminho de volta da normalização, recebe um numpy
    """
    return (dados * desvio_padrao) + media
