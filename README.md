# 📊 Dashboard de Análise de Salários

Este é um projeto de análise de dados de salários na área de tecnologia

## 📂 Organização do Projeto

Este repositório está organizado de forma a separar o processo de análise e preparação de dados da aplicação final.

* ### **Aplicação Principal (`dashbord.py`)**
  Este é o script que gera e executa o **dashboard interativo** com Streamlit. Ele representa o produto final do projeto e importa os dados já processados a partir do pipeline de tratamento.

* ### **Pipeline de Dados (`tratamento.py`, `programa.py`)**
  Esses dois arquivos trabalham em conjunto para formar o pipeline de dados. Eles são responsáveis pela **carga, limpeza e transformação** dos dados brutos em um formato limpo e pronto para análise. A função gerada aqui é a única dependência externa do `dashbord.py`.

* ### **Análise Exploratória (Outros Arquivos)**
  Os demais scripts no repositório contêm a **Análise Exploratória de Dados (EDA)**. Eles foram utilizados na fase de estudo para investigar o dataset, testar hipóteses e gerar os primeiros insights com bibliotecas como Matplotlib e Seaborn. **Estes arquivos são independentes e não são executados pelo dashboard**, servindo como um registro do processo de desenvolvimento e descoberta.

## 🛠️ Tecnologias Utilizadas

* **Análise de Dados:**
    * Pandas
    * Numpy

* **Visualização de Dados e Dashboard:**
    * Streamlit
    * Plotly
    * Matplotlib
    * Seaborn

* **Utilitários:**
    * PyCountry

## 🚀 Acessar o Aplicativo Online

Acesse a versão interativa do dashboard no Streamlit Cloud através do link abaixo:

**[➡️ Clique aqui para abrir o app!](https://imersaodedados-projeto.streamlit.app/)**