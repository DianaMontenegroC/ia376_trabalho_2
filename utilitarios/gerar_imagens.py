"""
Aquivo com a função que faz o download dos dados e passa para um DataFrame pandas
"""

import os
from pathlib import Path

import pandas as pd
from plotnine import ggplot, aes, geom_histogram, geom_point, geom_line, labs, theme_minimal

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from utilitarios.caminhos import imagens_dados # Só funciona quando executado do jupyter notebook


######################################################################

def histograma(dados, coluna:str, salvar_em:str, bins:int = 24) -> None:
    """
    Histograma da distribuição dos dados
    """
    grafico = (ggplot(dados, aes(x = coluna))
               + geom_histogram(bins = bins, fill = "steelblue", color = "black", alpha = 0.7)
               + labs(title = f"Histograma de {coluna}", x = coluna, y = "Frequência"))
    
    grafico.save(salvar_em)

def histograma_dos_erros(dados:list, salvar_em:str, nome_coluna:str = "[nome_coluna]", bins:int = 24) -> None:
    """
    Histograma dos erros
    """
    dados = pd.DataFrame({"erros":dados})
    grafico = (ggplot(dados, aes(x = "erros"))
               + geom_histogram(bins = bins, fill = "steelblue", color = "black", alpha = 0.7)
               + labs(title = f"Histograma dos Erros\nModelo: {nome_coluna}", x = "Erros", y = "Frequência"))
    
    grafico.save(salvar_em, width = 6, height = 3, dpi = 300)


def grafico_regressao_univariada(dados, X:str, y:str, real_y:list, salvar_em:str) -> None:
    """
    Regressão univariada
    """
    dados_plot = dados.copy()
    dados_plot["Predito"] = real_y

    # Gráfico
    grafico = (ggplot(dados_plot)
               + geom_point(aes(x = X[0], y = y, color = '"Observado"'), alpha = 0.3)
               + geom_line(aes(x = X[0], y = "Predito", color = '"Predição"'), size = 1.6)
               + labs(title = f"Regressão Univariada (X: {X[0].title()} | y: {y.title()})",
                      x = X[0], y = y))

    #grafico.show()
    grafico.save(salvar_em, width = 6, height = 3, dpi = 300)


def grafico_3d_multiplos_angulos(dados, x:str, y:str, z:str, titulo = "Visualização 3D"):
    """
    Gera vizualização 3d
    """
    fig = plt.figure(figsize = (12, 12))

    pos = [[0, -i*12.65 -0.1] for i in range(0, 8)]
    pos.extend([[20+i*20, -90] for i in range(4)])

    for i, (elev, azim) in enumerate(pos):
        ax = fig.add_subplot(3, 4, i + 1, projection='3d')  # índice começa em 1
        ax.scatter(dados[y], dados[x], dados[z],
                   c = dados[z], cmap="viridis", s=10)

        ax.view_init(elev=elev, azim=azim)
        ax.set_title(f"Elev: {elev}°, Azim: {azim}°", fontsize=10)
        ax.set_xlabel(y.title())
        ax.set_ylabel(x.title())
        ax.set_zlabel(z.title())
        ax.tick_params(labelsize = 6)

    fig.suptitle(titulo, fontsize=14)
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig(Path(imagens_dados, f"vizualizacao_{x}_{y}_{z}"))
    plt.show()
