# Consulta de Nomes no IBGE

Este projeto permite consultar a frequência de nomes no Brasil utilizando a **API de Censos do IBGE (v2/censos/nomes)**, com visualização em tabela e gráfico, através de uma interface web interativa com **Streamlit**.

## Funcionalidades

* Visualização dos resultados em:

  * **Tabela** interativa (`pandas` + `st.dataframe`)
  * **Gráfico de linha** mostrando a evolução ao longo dos anos
* Tratamento de casos onde não há resultados para o nome ou estado selecionado.
* Estrutura modular, com funções reutilizáveis para:

  * Fazer requisições HTTP (`requests`)
  * Organizar dados por período (`dict`)
  * Retornar informações estruturadas para exibição
* **Timeout** nas requisições para evitar travamentos da aplicação.

## Tecnologias

* **Python 3.x**
* Bibliotecas:

  * `requests` → requisições HTTP
  * `pandas` → manipulação e visualização de dados
  * `streamlit` → interface web interativa
  * `pprint` → exibição organizada dos dados no terminal (para testes)

## Como usar

### Localmente

1. Clone o repositório:

```bash
git clone https://github.com/seu_usuario/seu_repositorio.git
cd seu_repositorio
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute o app:

```bash
streamlit run api_ibge_pratica.py
```

## Hospedado em:

https://apiibge.streamlit.app/

## Aprendizados

* Consumo de **APIs públicas** e tratamento de respostas JSON.
* Criação de **interfaces web interativas** com Streamlit.
* Visualização de dados com **tabelas e gráficos**.
* Estruturação de projetos Python para **fácil manutenção e escalabilidade**.
