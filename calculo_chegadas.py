
import os
import pandas as pd

caminho = r"F:\Projeto Engenharia de Dados - Power BI\camada_stage"

base = []
for arquivo in os.listdir (caminho):
    if arquivo.endswith(".csv"):
        diretorio = os.path.join(caminho, arquivo)
        df = pd.read_csv(diretorio, sep=';', encoding='latin-1')
        base.append(df)

geral = pd.concat(base, ignore_index=True)        


fato_ano = geral.groupby('ano')['chegadas'].sum().reset_index()
fato_ano.to_csv(r"F:\Projeto Engenharia de Dados - Power BI\camada_final\fato_chegadas_ano.csv",
                sep=';', index=False, encoding='latin-1')

fato_pais_ano = geral.groupby(['pais', 'ano'])['chegadas'].sum().reset_index()
fato_pais_ano.to_csv(r"F:\Projeto Engenharia de Dados - Power BI\camada_final\fato_chegadas_pais_ano.csv",
                     sep=';', index=False, encoding='latin-1')


fato_uf_ano = geral.groupby(['uf', 'ano'])['chegadas'].sum().reset_index()
fato_uf_ano.to_csv(r"F:\Projeto Engenharia de Dados - Power BI\camada_final\fato_chegadas_uf_ano.csv",
                   sep=';', index=False, encoding='latin-1')


