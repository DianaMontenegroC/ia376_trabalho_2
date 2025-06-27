"""
Aquivo com a função que faz o download dos dados e passa para um DataFrame pandas
"""

import os
from pathlib import Path
import requests
import zipfile

from pandas import DataFrame, read_csv

# Próprios
import utilitarios.caminhos as caminho # Só funciona quando executo do jupyter

######################################################################

def download_dados() -> "DataFrame":
    """
    Função que faz o donwload dos dados
    """
    link:str = "https://drive.google.com/file/d/1_sBRn7oCu_ny4kIRSQbZjxqKOi1_xmyw/view?usp=sharing"

    def baixar_arquivo_drive(file_id, nome_destino):
        print(f"Baixando arquivo de {file_id} para pasta {nome_destino}")
        
        URL:str = "https://docs.google.com/uc?export=download"

        session = requests.Session()
        resposta = session.get(URL, params= {"id": file_id}, stream=True)

        for chave, valor in resposta.cookies.items():
            if chave.startswith("download_warning"):
                resposta = session.get(URL, params = {"id": file_id, "confirm": valor}, stream = True)
                break

        with open(nome_destino, "wb") as f:
            for chunk in resposta.iter_content(32768):
                if chunk:
                    f.write(chunk)

    salvar_como:str = "dados.zip"
    file_id:str = "1_sBRn7oCu_ny4kIRSQbZjxqKOi1_xmyw"
    salvar_zip = Path(caminho.dados, salvar_como)
    if not salvar_como in os.listdir(caminho.dados):
        baixar_arquivo_drive(file_id, salvar_zip)
    else:
        print(f"'{salvar_como}' já existe em '{caminho.dados}' !")

    nome_arquivo:str = "dados_IA376.csv"
    if not nome_arquivo in os.listdir(caminho.dados):
        with zipfile.ZipFile(salvar_zip, "r") as zip_ref:
            zip_ref.extractall(caminho.dados)
            print(f"ZIP estraido!")
    else:
        print(f"ZIP já foi estraido!")

    return read_csv(Path(caminho.dados, nome_arquivo))
