import pandas as pd
import streamlit as st
import plotting

# Carregar os dados com pandas
# df = Dataframe do pandas (Nome genérico para funções no pandas)
df  = pd.read_csv('intensivo_python/Aula03_Analise_de_Dados/dados_cartao_convertido.csv')
# Adicionar coluna com os nomes dos titulares dos cartões
df['Titular'] = df['NumeroCartao'].map({
    7840517590708225: 'João',
    7142474765870246: 'Ana'
})

# Tabela = Dataframe (df)
# Adicionar a coluna NumeroCartao para string
df['NumeroCartao'] = df['NumeroCartao'].astype(str) # Converte para texto
# Converter a coluna data_compra para datetime
df['data_compra'] = pd.to_datetime(df['data_compra']) # Converte para data e hora

# Análise dos dados
valor_total_cartao = df['ValorCompra'].sum() # Soma todas os valores da coluna "ValorCompra"
valor_gasto_por_titular = df.groupby('Titular')['ValorCompra'].sum().reset_index() # Soma todos os valores de cada titular
valor_gasto_por_categoria = df.groupby('categoria')['ValorCompra'].sum().reset_index() # Soma todos os valores de cada categoria

# Criação dos gráficos
fig_barra_categoria = plotting.grafico_gastos_por_categoria(valor_gasto_por_categoria) # Criar um gráfico de barra para mostrar os valores por categoria
fig_barra_categoria_pizza = plotting.grafico_gastos_por_categoria_pie(valor_gasto_por_categoria) # Criar um gráfico de pizza "pie" para mostrar os valores por categoria
fig_barra_titular = plotting.grafico_gastos_por_titular(valor_gasto_por_titular) # Criar um gráfico de barra para mostrar os valores por titular

gastos_ao_longo_do_tempo = df.groupby('data_compra')['ValorCompra'].sum().reset_index()
fig_linha = plotting.grafico_gastos_ao_longo_do_tempo(gastos_ao_longo_do_tempo)

# Interface da página em Streamlit
st.set_page_config(layout="centered")
st.title('Compras de Cartão de Crédito')

st.header('Informações Gerais')
st.write(f'Valor total gasto: R$ {valor_total_cartao:.2f}')

st.header('Valor Gasto por Titular')
st.dataframe(valor_gasto_por_titular)

st.header('Valor Gasto por Categoria')
st.dataframe(valor_gasto_por_categoria)

st.header('Gráficos')
st.subheader('Gastos por Categoria')
st.plotly_chart(fig_barra_categoria) # "plotly_chart": Pega um dado que está armazenado entre parenteses e plota na tela do site

st.subheader('Gastos por Titular')
st.plotly_chart(fig_barra_titular)

st.subheader('Valor Total Gasto ao Longo do Tempo')
st.plotly_chart(fig_linha)

# Interface do Streamlit
st.title('Todas as Compras no Cartão de Crédito')
st.header('Informações Gerais')
st.dataframe(df)
