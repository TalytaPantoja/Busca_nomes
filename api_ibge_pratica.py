import requests
from pprint import pprint
import sys
sys.stdout.reconfigure(encoding='utf-8')

import streamlit as st
import pandas as pd

# Função para fazer request (otimiza o código)
def fazer_request(url, params=None):
    try:
        resposta = requests.get(url, params=params, timeout=5)
        resposta.raise_for_status()
    except requests.HTTPError as e:
        print (f'Erro na requisição: {e}')
        resultado = None
    else:
        resultado = resposta.json()
    return resultado

def busca_nome(nome, localidade_id):
    url = f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}'
    params = {'localidade': localidade_id}  # input pelo usuário

    nomes_estado = fazer_request(url, params=params)      
    if not nomes_estado:
        return None

    dict_nomes = {}
    for dados in nomes_estado[0]['res']:
        periodo = dados['periodo']
        frequencia = dados['frequencia']
        formatacao = periodo.replace('[', '').replace(']', '').replace(',', '-')
        dict_nomes[formatacao] = frequencia
    return dict_nomes

def busca_estado():
    url = 'https://servicodados.ibge.gov.br/api/v1/localidades/municipios'
    params = {'view': 'nivelado'} 

    estados = fazer_request(url, params=params)
    if not estados:
        return None

    dict_estados = {}  # salva estados numa lista
    for dados in estados:
        nome_estados = dados['UF-nome']
        id_estados = dados['UF-id']
        dict_estados[nome_estados] =  id_estados
    return dict_estados

def main():
    st.title('WebApp Busca Nomes')
    st.write('Dados do IBGE (Fonte: https://servicodados.ibge.gov.br/api/docs/nomes?versao=2)')

    nome = st.text_input('Consulte um nome: ')
    if not nome:
        st.stop()
    
    busca = busca_estado()
    localidade = st.selectbox('Escolha a localidade: ', list(busca.keys()))

    if localidade:
        localidade_id = busca[localidade]  # pega o ID do estado selecionado
        dict_busca = busca_nome(nome, localidade_id)
        
        if dict_busca:
            st.write(f"Resultados para: **{nome}** no estado: **{localidade}**")

            col1, col2 = st.columns([0.3, 0.7])
            with col1:
                df = pd.DataFrame.from_dict(dict_busca, orient="index", columns=['Frequência'])
                df.index.name = 'Anos'
                st.dataframe(df)
            with col2:
                st.line_chart(df)
        else:
            st.warning("Nenhum dado encontrado para este nome/estado.")

if __name__ == '__main__':
    main()