from sys import path
import pandas as pd

# Bibliotecas para customização e exibição dos gráficos gerados
import matplotlib.pyplot as plt

# Biblioteca para criação e customização dos gráficos
import seaborn as sns 

# Biblioteca para criação de gráficos interativos
import plotly.express as px

path.append('../IMERSAODEDADOS/02')

from tratamento import carregar_df_limpo

df = carregar_df_limpo()

# Selecionando a coluna 'senioridade', realizando a contagem de cada valor, representando como um gráfico de barras e adicionando um título a ele
df['senioridade'].value_counts().plot(kind='bar', title = 'distribuição de senioridade')

# Exibindo gráficos gerados
plt.show()

# Gerando gráfico 
sns.barplot(data = df, x = 'senioridade', y = 'salario_em_usd')
plt.show()

# Gerando gráfico melhor configurado
plt.figure(figsize=(8, 5)) # Dimensões
sns.barplot(data=df, x = 'senioridade', y = 'salario_em_usd') # Base de dados, informação do eixo x e informação do eixo y
plt.title('Salário por senioridade') # Título
plt.xlabel('Senioridade') # Título do eixo x
plt.ylabel('salario médio anual (em dólar)') # Título do eixo y
plt.show()

# Agrupando dados pelo parâmetro especificado, calculando média do outro campo especificado e ordenando valores em ordem decrescente

print(df.groupby('senioridade')['salario_em_usd'].mean().sort_values(ascending=False))

ordem = df.groupby('senioridade')['salario_em_usd'].mean().sort_values(ascending=False).index # Extrai apenas os índices de senioridade

# Gráfico anteior, agora, ordenado em ordem descrescente por senoridade
plt.figure(figsize=(8, 5)) # Dimensões
sns.barplot(data=df, x = 'senioridade', y = 'salario_em_usd', order= ordem) # Base de dados, informação do eixo x e informação do eixo y
plt.title('Salário por senioridade') # Título
plt.xlabel('Senioridade') # Título do eixo x
plt.ylabel('salario médio anual (em dólar)') # Título do eixo y
plt.show()

plt.figure(figsize=(8, 4))

# Gerar histograma de frequência do campo 'salario_em_usd'
sns.histplot(df['salario_em_usd'], bins = 30, kde = True) # Bins define a quantidade de barras(intervalos) do histograma de frequência e kde define se irá haver contorno indicando a forma do gráfico

plt.title("Frequência dos salários anuais")
plt.xlabel('Salário em USD')
plt.ylabel('Frequência')
plt.show()

# Gerar boxplot
plt.figure(figsize=(8, 5))
sns.boxplot(x = df['salario_em_usd'])
plt.title('Boxplot salário')
plt.xlabel('salário em usd')
plt.show()

ordem_senioridade = ['Junior', 'Pleno', 'Senior', 'Executivo']
plt.figure(figsize = (8, 5))
sns.boxplot(x='senioridade', y = 'salario_em_usd', data = df, order=ordem_senioridade)
plt.title('Boxplot senioridade')
plt.xlabel('Senioridade')
plt.show()

# Atribuição de cores
plt.figure(figsize = (8, 5))
sns.boxplot(x='senioridade', y = 'salario_em_usd', data = df, order=ordem_senioridade, palette = 'Set2', hue= 'senioridade') # Definição de paleta de cores para a categoria especificada
plt.title('Boxplot senioridade')
plt.xlabel('Senioridade')
plt.show()

#Criação de gráfico interativo
senioridade_media_salario = df.groupby('senioridade')['salario_em_usd'].mean().sort_values(ascending = False).reset_index()

#Criação do gráfico
fig = px.bar(senioridade_media_salario, x = 'senioridade', y = 'salario_em_usd', title = "Média salarial por senioridade", labels ={'senioridade': 'Nível de senioridade', 'salario_em_usd': 'Média salarial anual'})

# Criando documento HTML para apresentar o gráfico iterativo ('fig.show' também apresentaria, só que sem criar o documento HTML )
fig.write_html("grafico_interativo.html")

# Gerando gráfico de pizza/torta
remoto_contagem = df['remoto'].value_counts().reset_index()
remoto_contagem.columns = ['tipo_trabalho', 'quantidade']
fig2 = px.pie(remoto_contagem, 
              names = 'tipo_trabalho', 
              values = 'quantidade',
              title = 'proporção dos tipos de trabalho'
              )

fig2.write_html("grafico_pizza.html")

# Gerando gráfico de rosca
fig3 =  px.pie(remoto_contagem, 
              names = 'tipo_trabalho', 
              values = 'quantidade',
              title = 'proporção dos tipos de trabalho',
              hole = 0.5
              )
fig3.update_traces(textinfo = 'percent+label') # Adicionando ao gráfico o título da coluna correspondente

fig3.write_html("gráfico_rosca.html")