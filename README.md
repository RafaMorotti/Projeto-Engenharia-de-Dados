# 🌍 Análise de Chegadas de Turistas Internacionais ao Brasil (2015–2024)

## Sobre o Projeto

Pipeline de tratamento e consolidação de dados públicos de turismo internacional, extraídos do portal **gov.br**, cobrindo o período de **2015 a 2024**.

O objetivo foi transformar 10 arquivos brutos em bases analíticas limpas e estruturadas, prontas para consumo em ferramentas de visualização ou análises futuras.

---

## 📁 Fonte dos Dados

- **Portal:** [gov.br – Ministério do Turismo](https://www.gov.br/turismo)
- **Período:** 2015 a 2024
- **Formato original:** CSV / Excel
- **Conteúdo:** Chegadas de turistas internacionais ao Brasil, segmentadas por país de origem, UF de entrada, via de acesso e mês

---

## ⚙️ O que o Script Faz

1. Lê e consolida os 10 arquivos de entrada em um único DataFrame
2. Padroniza colunas, tipos de dados e nomenclaturas
3. Trata valores nulos e inconsistências
4. Gera 3 arquivos analíticos finais:

| Arquivo de Saída | Descrição |
|---|---|
| `fato_chegadas_ano.csv` | Total de chegadas agregado por ano |
| `fato_chegadas_pais_ano.csv` | Chegadas por país de origem e ano |
| `fato_chegadas_uf_ano.csv` | Chegadas por UF de entrada e ano |

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **Pandas** – leitura, tratamento e consolidação dos dados
- **openpyxl** – leitura dos arquivos Excel originais

---

## ▶️ Como Executar

```bash
# Clone o repositório
git clone https://github.com/RafaMorotti/<nome-do-repositorio>

# Instale as dependências
pip install pandas openpyxl

# Execute o script
python tratamento_turismo.py
```

---

## 📊 Exemplo dos Dados Tratados

| Continente | País | UF | Via de Acesso | Ano | Mês | Chegadas |
|---|---|---|---|---|---|---|
| África | Angola | Acre | Terrestre | 2015 | Janeiro | 2 |
| América Central e Caribe | Cuba | SP | Aéreo | 2019 | Março | 145 |

---

## 💡 Aprendizados

- Consolidação de múltiplos arquivos com estrutura heterogênea
- Tratamento de dados públicos com inconsistências reais
- Geração de bases analíticas segmentadas para diferentes granularidades

---

## 👤 Autor

**Rafael Morotti**  
[LinkedIn](https://www.linkedin.com/in/rafael-morotti) | [GitHub](https://github.com/RafaMorotti) | rafa.morotti@gmail.com
