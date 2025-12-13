import pandas as pd
import os


def extrair(caminho_arquivo):
    saida_leitura = pd.read_csv(
        caminho_arquivo,
        sep=';',
        encoding='latin-1',
        engine='python'
    )
    return saida_leitura

def transformar(saida_leitura):
    # 1) Começa copiando o DataFrame de entrada
    saida_transformada = saida_leitura.copy()
    # 2) Renomear colunas
    saida_transformada = saida_transformada.rename(columns={
        'Continente': 'continente',
        'Ordem continente': 'ordem_continente',
        'País': 'pais',
        'Ordem país': 'ordem_pais',
        'UF': 'uf',
        'Ordem UF': 'ordem_uf',
        'Via de acesso': 'via_acesso',
        'Ordem via de acesso': 'ordem_via_acesso',
        'ano': 'ano',
        'Mês': 'mes',
        'Ordem mês': 'ordem_mes',
        'Chegadas': 'chegadas'
     })

    # 3) Garantir tipos

    saida_transformada['ano'] = saida_transformada['ano'].astype(int)
    saida_transformada['chegadas'] = saida_transformada['chegadas'].astype(int)
    
    return saida_transformada

def carrega(dados_tratados, caminho_destino):
    dados_tratados.to_csv(
        caminho_destino,
        sep=';',
        index=False,
        encoding='latin-1'
    )
    
pasta_raw = r"F:\Projeto Engenharia de Dados - Power BI\camada_raw"

for nome_arquivo in os.listdir(pasta_raw):
    if nome_arquivo.endswith(".csv"):
        caminho = os.path.join(pasta_raw, nome_arquivo)

        dados_brutos = extrair(caminho)
        dados_tratados = transformar(dados_brutos)

        caminho_destino = caminho.replace("camada_raw", "camada_stage").replace(".csv", "_tratado.csv")
        carrega(dados_tratados, caminho_destino)

        print(f"Processado: {nome_arquivo}")


# validação da mudança somando uma coluna do arquivo final
# total_chegadas_2015 = dados_tratados['chegadas'].sum()
# print(total_chegadas_2015)




