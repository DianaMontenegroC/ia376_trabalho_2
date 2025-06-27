"""
Arquivo com todos os caminhos de diretórios usados no trabalho.
"""

import os
from pathlib import Path


######################################################################

dados = Path("dados")

resultados = Path("resultados")

# Imagens
imagens = Path(resultados, "imagens")

imagens_dados = Path(imagens, "distribuicao_dos_dados")

imagens_regressao = Path(imagens, "regressao")
imagens_rede_neural = Path(imagens, "rede_neural")

imagens_regressao_previsao = Path(imagens_regressao, "previsao")
imagens_rede_neural_previsao = Path(imagens_rede_neural, "previsao")

imagens_regressao_histograma = Path(imagens_regressao, "histograma_dos_erros")
imagens_rede_neural_histograma = Path(imagens_rede_neural, "histograma_dos_erros")

# Tabelas
tabelas = Path(resultados, "tabelas")

tabelas_regressao = Path(tabelas, "regressao")
tabelas_rede_neural = Path(tabelas, "rede_neural")

# Backup
backup = Path(resultados, "backup")
backup_pesos_rede_neural = Path(backup, "pesos_rede_neural")

######################################################################

todos_caminhos = [dados,
                  resultados,
                  imagens,
                  imagens_dados,
                  imagens_regressao, imagens_rede_neural,
                  imagens_regressao_previsao, imagens_rede_neural_previsao,
                  imagens_regressao_histograma, imagens_rede_neural_histograma,               
                  tabelas,
                  tabelas_regressao, tabelas_rede_neural,
                  backup,
                  backup_pesos_rede_neural]

for caminho in todos_caminhos:
    caminho.mkdir(parents = True, exist_ok = True)

