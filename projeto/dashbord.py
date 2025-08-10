# Biblioteca para criação e configuração de aplicações web
import streamlit as st # 'Criar' página = terminal: streamlit run programa.py
import pandas as pd
import plotly.express as px

# Biblioteca para conversão de siglas de país para formato ISO-3
import pycountry

from tratamento import carregar_df_limpo

df = carregar_df_limpo()

# Configuração da página
st.set_page_config(
    page_title = 'Dashbord',
    page_icon = '📊',
    layout = 'wide',
)

# Definindo e configurando barra lateral
st.sidebar.header('🔍 Filtros')

# Adicionar filtro de Ano
anos_disponiveis = sorted(df['ano'].unique())
anos_selecionados = st.sidebar.multiselect('Ano', anos_disponiveis, default= anos_disponiveis)

# Adicionar filtro por Senioridade
senioridades_disponiveis = sorted(df['senioridade'].unique())
senioridades_selecionadas = st.sidebar.multiselect('Senioridade', senioridades_disponiveis, default = senioridades_disponiveis)

# Adicionar filtro por Tipo de Contrato
contratos_disponiveis = sorted(df['contrato'].unique())
contratos_selecionados = st.sidebar.multiselect('Contrato', contratos_disponiveis, default = contratos_disponiveis)

# Adicionar filtro por Tamanho da Empresa
tamanhos_disponiveis = sorted(df['tamanho_empresa'].unique())
tamanhos_selecionados = st.sidebar.multiselect('Tamanho da empresa', tamanhos_disponiveis, default = tamanhos_disponiveis)

# Filtragem do dataframe com bae nas seleções feitas na barra lateral
df_filtrado = df[
    (df['ano'].isin(anos_selecionados)) &
    (df['senioridade'].isin(senioridades_selecionadas)) &
    (df['contrato'].isin(contratos_selecionados)) &
    (df['tamanho_empresa'].isin(tamanhos_selecionados))
]

# Conteúdo principal
st.title("🎲 dashbord de Análise de salários na Area de Dados")
st.markdown('Explore os dados salariais na área de dados nos últimos anos. Utilize os filtos à esquerda para refinar sua análise')

st.subheader('Métricas gerais') 

if not df_filtrado.empty:
    salario_medio = df_filtrado['salario_em_usd'].mean()
    salario_maximo = df_filtrado['salario_em_usd'].max()
    total_registros = df_filtrado.shape[0]
    cargo_mais_frequente = df_filtrado['cargo'].mode()[0]

else:
    salario_media, salario_mediano, salario_maximo, total_registros, cargo_mais_comum = 0, 0, 0, 0,""

col1, col2, col3, col4 = st.columns(4)
col1.metric('Salário médio', f"${salario_medio:,.0f}")
col2.metric('Salário máximo', f"${salario_maximo:,.0f}")
col3.metric('Total de registros', f"${total_registros:,}")
col4.metric('Cargo mais frequente', cargo_mais_frequente)

st.subheader('Gráficos')

# Exibição dos gráficos
col_graf1, col_graf2 = st.columns(2)

with col_graf1:
    if not df_filtrado.empty:
        top_cargos = df_filtrado.groupby('cargo')['salario_em_usd'].mean().nlargest(10).sort_values(ascending = True).reset_index()
        grafico_cargos = px.bar(
        top_cargos, 
        x = 'salario_em_usd',
        y = 'cargo',
        orientation = 'h',
        title = 'Top 10 cargos por salário médio',
        labels = {'usd': 'Media salarial anual (USD)', 'cargo': ''}
        )

        # Configurando posição do gráfico em relação aos eixos x e y
        grafico_cargos.update_layout(title_x = 0.1, yaxis={'categoryorder': 'total ascending'})

        # Exibição do gráfico
        st.plotly_chart(grafico_cargos, use_container_width=True)
        
    else:
        st.warning("Nenhum dado para exibir no gráfico de cargos")

with col_graf2:
    if not df_filtrado.empty:
        grafico_hist = px.histogram(
            df_filtrado, 
            x = 'salario_em_usd',
            nbins=30,
            title ='Distribuição de salários anuais',
            labels={'salario_em_usd': 'Faixa salarial(USD)', 'count': ''}
        )
        grafico_hist.update_layout(title_x= 0.1)
        st.plotly_chart(grafico_hist, use_container_width=True)
        
    else:
        st.warning("Nenhum dado para exibir no gráfico de distribuição")

col_graf3, col_graf4 = st.columns(2)

with col_graf3:
    if not df_filtrado.empty:
        remoto_contagem = df_filtrado['remoto'].value_counts().reset_index()
        remoto_contagem.columns = ['tipo_trabalho', 'quantidade']
        grafico_remoto = px.pie(
            remoto_contagem, names='tipo_trabalho',
            values='quantidade',
            title ='Proporção dos tipos de trabalho',
            hole = 0.5
        )
        grafico_remoto.update_traces(textinfo='percent+label')
        grafico_remoto.update_layout(title_x=0.1)
        st.plotly_chart(grafico_remoto, use_container_width=True)
    
    else:
        st.warning("Nenhum dado para exibir no gráfico dos tipos de trabalho")

# Criar gráfico em formato de mapa

# Função para converter ISO-2 para ISO-3
def iso2_to_iso3(code):
    try:
        return pycountry.countries.get(alpha_2=code).alpha_3
    except:
        return None
    
# Criar nova coluna com código ISO-3
df_filtrado['residencia_iso3'] = df_filtrado['residencia_funcionario'].apply(iso2_to_iso3)

# Gerar mapa
with col_graf4:
    if not df_filtrado.empty:
        df_ds = df_filtrado[df_filtrado['cargo'] == 'Data Scientist']
        media_ds_pais = df_ds.groupby('residencia_iso3')['salario_em_usd'].mean().reset_index()
        grafico_paises = px.choropleth(
        media_ds_pais,
        locations='residencia_iso3',
        color='salario_em_usd',
        color_continuous_scale='rdylgn',
        title='Salário médio de cientista de dados por país',
        labels={'salario_em_usd': 'salário médio(USD)', 'residencia_iso3': 'Pais'}
    )
        grafico_paises.update_layout(title_x=0.1)
        st.plotly_chart(grafico_paises, use_container_width=True)

    else:
        st.warning("Nenhum dado para exibir no gráfico dos países")
    
st.subheader('Dados detalhados')
st.dataframe(df_filtrado)

# Criar e salvar arquivo do dataframe
df_filtrado.to_csv('dados-imersao-final.csv', index=False)

