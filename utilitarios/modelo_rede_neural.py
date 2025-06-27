"""
Aquivo com a função que faz o download dos dados e passa para um DataFrame pandas
"""

import os
from pathlib import Path

import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, Dense, LeakyReLU
from tensorflow.keras.callbacks import EarlyStopping
import numpy as np

from utilitarios.caminhos import tabelas_rede_neural, backup_pesos_rede_neural # Só funciona quando executado do jupyter notebook


tf.config.experimental.enable_op_determinism()
tf.random.set_seed(2025)
######################################################################

def rede_neural(dados, X:list, y:str, neuronios:int = 32, monitoramento:str = "val_loss", validacao:float = 0.2, slope:float = 0.01):
    """
    Treina modelo de rede neural
    """
    nomes_X:list = X
    nome_y:str = y
    
    X = np.array(dados[X])
    y = np.array(dados[y])

    # Caminhos
    nome_base:str = f"historico_{'+'.join(nomes_X)}-{nome_y}"
    caminho_pesos = Path(backup_pesos_rede_neural, f"{nome_base}.weights.h5")
    caminho_historico = Path(tabelas_rede_neural, f"{nome_base}.csv")
    
    # Rede
    modelo = Sequential([Input(shape = (X.shape[1],)),
                         Dense(neuronios),
                         LeakyReLU(negative_slope = slope),
                         Dense(1)])

    modelo.compile(optimizer = "adam",
                   loss = "mse",
                   metrics = ["mse", "mae"])

    if caminho_pesos.exists():
        modelo.load_weights(caminho_pesos)
    else:
        # Treina o modelo
        early_stop = EarlyStopping(monitor = monitoramento,
                                   patience = 30,
                                   restore_best_weights = True)

        historico = modelo.fit(X, y,
                               epochs = 1000, # Número máximo de épocas
                               batch_size = 8,
                               validation_split = validacao,
                               callbacks = [early_stop],
                               verbose=0)

        # Salvando historico da loss
        df_historico = pd.DataFrame(historico.history)
        df_historico.to_csv(Path(caminho_historico, index = False))

        # Salva os pesos
        modelo.save_weights(caminho_pesos)

    return modelo

def predicao_rede_neural(dados, modelo, X:list) -> list:
    """
    Faz predição dos modelos
    """
    X = np.array(dados[X])

    return modelo.predict(X, verbose = 0)
