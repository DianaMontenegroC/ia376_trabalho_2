"""
Arquivo com funções estatísticas 
"""

import os
from pathlib import Path

import pandas as pd

import utilitarios.caminhos as caminho # Só funciona quando executo do jupyter

######################################################################

def calcular_r_quadrado(dados:"DataFrame", dicionario_memoria:"dict", nome_complementar:str = "") -> "DataFrame":
    """
    Retorna e salva um dataframe do R^2 para os modelos
    """

    tabela:dict = {"tipo":[], "entradas":[], "saida":[], "r^2":[], "mse":[]}

    print(f"Criando tabela para:")
    for index, parametros in enumerate(dicionario_memoria):
        print(f"\tf({', '.join(parametros['X'])}) -> {parametros['y']}")
        
        media:float = dados[parametros["y"]].mean()
        dicionario_memoria[index]["r^2_regressao"] = 1 - sum([i*i for i in parametros["erros_regressao"]])/sum([(real - media)*(real - media) for real in dados[parametros["y"]]])
        dicionario_memoria[index]["r^2_rede_neural"] = 1 - sum([i*i for i in parametros["erros_rede_neural"]])/sum([(real - media)*(real - media) for real in dados[parametros["y"]]])

        # Adicionando itens na tabela
        tabela["tipo"].append("Regressão")
        tabela["entradas"].append(", ".join(parametros["X"]))
        tabela["saida"].append(parametros["y"])
        tabela["r^2"].append(dicionario_memoria[index]["r^2_regressao"])
        tabela["mse"].append(dicionario_memoria[index]["mse_regressao"])
        
        tabela["tipo"].append("Rede Neural")
        tabela["entradas"].append(", ".join(parametros["X"]))
        tabela["saida"].append(parametros["y"])
        tabela["r^2"].append(dicionario_memoria[index]["r^2_rede_neural"])
        tabela["mse"].append(dicionario_memoria[index]["mse_rede_neural"])
        
    print()

    tabela = pd.DataFrame(tabela)
    tabela.to_csv(Path(caminho.tabelas, f"r_quadrado{nome_complementar}.csv"))

    return tabela


def criar_tabela(dados:list, nome:str) -> None:
    """
    Cria tabela por meio de dicionario
    """    
    dicionario_final:dict = {}
    for index in range(len(dados)):
        dicionario = dados[index]
        for coluna in dicionario.keys():
            if not coluna in dicionario_final:
                dicionario_final[coluna] = []
        
            if type(dicionario[coluna]) != list:
                dicionario_final[coluna].append(dicionario[coluna])
            else:
                dicionario_final[coluna].append(", ".join(dicionario[coluna]))

    df = pd.DataFrame(dicionario_final)
    df.to_csv(Path(caminho.tabelas, nome), index = False)

