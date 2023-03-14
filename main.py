
import streamlit as st
import pandas as pd

@st.cache
def load_data():
    st.spinner(text='Carregando Banco de Dados...')
    return pd.read_csv("receita_federal_sample.csv").head(1000)

# def load_data():
#     st.spinner(text='Carregando Banco de Dados...')
#     dado = pd.read_csv('receita_federal_sample.csv')
#     return dado[dado['OPCAO_PELO_SIMPLES'] == 'S']


def filter_data(data,column1,value1,filtros,column2=0,value2=0,column3=0,value3=0,column4=0,value4=0):

    #--1 FILTER
    #-----------
    if filtros == 1:
        if (column1 == 'CNAE_FISCAL_PRINCIPAL') | (column1 == 'RAZAO_SOCIAL') | (column1 == 'CNPJ_BASICO') | (column1 == 'CNPJ_FULL'):
            data = data[data[column1].astype(str).str.startswith(str(value1))]
        else:
            data = data[data[column1] == value1]
    #--2 FILTERS
    #-----------
    elif filtros == 2:
        if (column1 == 'CNAE_FISCAL_PRINCIPAL') | (column1 == 'RAZAO_SOCIAL') | (column1 == 'CNPJ_BASICO') | (column1 == 'CNPJ_FULL'):
            data = data[(data[column1].astype(str).str.startswith(str(value1))) & \
                        (data[column2] == value2)]
        elif (column2 == 'CNAE_FISCAL_PRINCIPAL') | (column2 == 'RAZAO_SOCIAL') | (column2 == 'CNPJ_BASICO') | (column2 == 'CNPJ_FULL'):
            data = data[(data[column1] == value1) &\
                        (data[column2].astype(str).str.startswith(str(value2)))]
        else:
            data = data[(data[column1] == value1) & \
                        (data[column2] == value2)]
    #--3 FILTERS
    #-----------
    elif filtros == 3:
        if (column1 == 'CNAE_FISCAL_PRINCIPAL') | (column1 == 'RAZAO_SOCIAL') |( column1 == 'CNPJ_BASICO') | (column1 == 'CNPJ_FULL'):
            data = data[(data[column1].astype(str).str.startswith(str(value1))) & \
                        (data[column2] == value2) &
                        (data[column3] == value3)]
        elif (column2 == 'CNAE_FISCAL_PRINCIPAL') |( column2 == 'RAZAO_SOCIAL') | (column2 == 'CNPJ_BASICO') | (column2 == 'CNPJ_FULL'):
            data = data[(data[column1] == value1) & \
                        (data[column2].astype(str).str.startswith(str(value2))) &\
                        (data[column3] == value3)]
        elif (column3 == 'CNAE_FISCAL_PRINCIPAL') | (column3 == 'RAZAO_SOCIAL') | (column3 == 'CNPJ_BASICO') | (column3 == 'CNPJ_FULL'):
            data = data[(data[column3].astype(str).startswith(str(value3))) &\
                        (data[column1] == value1) &\
                        (data[column2] == value2)]
        else:
             data = data[(data[column1] == value1) &\
                         (data[column2] == value2) &\
                         (data[column3] == value3)]
    #--4 FILTERS
    #-----------
    elif filtros == 4:
        if (column1 == 'CNAE_FISCAL_PRINCIPAL') | (column1 == 'RAZAO_SOCIAL') | (column1 == 'CNPJ_BASICO') | (column1 == 'CNPJ_FULL'):
            data = data[(data[column1].astype(str).str.startswith(str(value1))) & \
                        (data[column3] == value3) &
                        (data[column4] == value4) &
                        (data[column2] == value2)]
        elif (column2 == 'CNAE_FISCAL_PRINCIPAL') | (column2 == 'RAZAO_SOCIAL') | (column2 == 'CNPJ_BASICO') | (column2 == 'CNPJ_FULL'):
            data = data[(data[column1] == value1) & \
                        (data[column2].astype(str).str.startswith(str(value2))) &
                        (data[column3] == value3) &
                        (data[column4] == value4)]
        elif (column3 == 'CNAE_FISCAL_PRINCIPAL') | (column3 == 'RAZAO_SOCIAL') | (column3 == 'CNPJ_BASICO') | (column3 == 'CNPJ_FULL'):
            data = data[(data[column3].astype(str).startswith(str(value3))) & \
                        (data[column1] == value1) & \
                        (data[column2] == value2) &
                        (data[column4] == value4)]
        elif (column4 == 'CNAE_FISCAL_PRINCIPAL') | (column4 == 'RAZAO_SOCIAL') | (column4 == 'CNPJ_BASICO') | (column4 == 'CNPJ_FULL'):
            data = data[(data[column4].astype(str).str.startswith(str(value4))) &\
                        (data[column1] == value1) &\
                        (data[column2] == value2) &\
                        (data[column3] == value3)]
        else:
            data = data[(data[column1] == value1) &\
                        (data[column2] == value2) &\
                        (data[column3] == value3) &\
                        (data[column4] == value4)]
    else:
        pass

    return data

def main():
#--PRIMARY FUNCTION TO THIS APP
    st.set_page_config(page_title="Filtra Banco de Dados Receita Federal", page_icon=":guardsman:", layout="wide")
    #--SET PAGE TITLE
    st.title("Filtra Banco de Dados Receita Federal (Apenas CNPJ ativo)")

    with st.spinner('Espere um momento...'):
        #--CALL FUNC LOAD DATA
        data = load_data()

    #--CREATE DICT WITH COLUMN TYPES TO USE BEST FILTERS
    dict_column = data.dtypes.to_dict()
    #--SEPARE COLUMNS TO FILTER
    columns = ['CNPJ_BASICO', 'DATA_DE_INICIO_ATIVIDADE', 'CNAE_FISCAL_PRINCIPAL', 'UF', 'MUNICIPIO', 'RAZAO_SOCIAL_NOME_EMPRESARIAL', 'PORTE_DA_EMPRESA', 'OPCAO_PELO_SIMPLES', 'OPCAO_PELO_MEI', "CNPJ_FULL"]
    #--CREATE DROPDOWN TO CHOOSE HOW MANY FILTERS
    filtros = st.selectbox('Quantos Filtros quer utilizar?', range(1,5))

    ##################
    #--  1 FILTER  --#
    ##################
    if filtros == 1:
        column1 = st.selectbox("Selecione coluna para filtrar", columns, key='1')
        #--CHECK TO SEE COLUMN TYPE
        if dict_column[column1] == 'object':
            value1 = str(st.text_input(f"Entre com o texto para filtrar pela coluna {column1}"))
        else:
            value1 = st.number_input(f'Entre com o valor para filtrar pela coluna {column1}', step=1, key='1.')
        #--CALL FUNC TO FILTER DATA BASED ON FILTERS
        filtered_data = filter_data(data, column1, value1, filtros)

    ##################
    #--  2 FILTER  --#
    ##################
    elif filtros == 2:
        column1 = st.selectbox("Selecione coluna para filtrar", columns, key='2')
        #--CHECK TO SEE COLUMN TYPE
        if dict_column[column1] == 'object':
            value1 = str(st.text_input(f"Entre com o texto para filtrar a coluna {column1}"))
        else:
            value1 = st.number_input(f'Entre com o valor para filtrar pela coluna {column1}', step=1, key='2.')

        column2 = st.selectbox("Selecione a segunda coluna para filtrar", columns, key='3')
        #--CHECK TO SEE COLUMN TYPE
        if dict_column[column2] == 'object':
            value2 = str(st.text_input(f"Entre com o texto para filtrar a coluna {column2}"))
        else:
            value2 = st.number_input(f'Entre com o valor para filtrar pela coluna {column2}', step=1, key='3.')
        #--CALL FUNC TO FILTER DATA BASED ON FILTERS
        filtered_data = filter_data(data, column1, value1, filtros, column2, value2)

    ##################
    #--  3 FILTER  --#
    ##################
    elif filtros == 3:
        column1 = st.selectbox("Selecione coluna para filtrar", columns, key='4')
        #--CHECK TO SEE COLUMN TYPE
        if dict_column[column1] == 'object':
            value1 = str(st.text_input(f"Entre com o texto para filtrar a coluna {column1}"))
        else:
            value1 = st.number_input('Entre com o valor para filtrar', step=1, key='4.')

        column2 = st.selectbox("Selecione a segunda coluna para filtrar", columns, key='5')
        #--CHECK TO SEE COLUMN TYPE
        if dict_column[column2] == 'object':
            value2 = str(st.text_input(f"Entre com o texto para filtrar a coluna {column2}"))
        else:
            value2 = st.number_input(f'Entre com o valor para filtrar pela coluna {column2}', step=1, key='5.')

        column3 = st.selectbox('Selecione terceira coluna para filtrar', columns, key='6')
        #--CHECK TO SEE COLUMN TYPE
        if dict_column[column3] == 'object':
            value3 = str(st.text_input(f"Entre com o texto para filtrar a coluna {column3}"))
        else:
            value3 = st.number_input(f'Entre com o valor para filtrar pela coluna {column3}', step=1, key='6.')
        #--CALL FUNC TO FILTER DATA BASED ON FILTERS
        filtered_data = filter_data(data, column1, value1, filtros, column2, value2, column3,\
                                    value3)

    ##################
    #--  4 FILTER  --#
    ##################
    elif filtros == 4:
        column1 = st.selectbox("Selecione coluna para filtrar", columns, key='7')
        #--CHECK TO SEE COLUMN TYPE
        if dict_column[column1] == 'object':
            value1 = str(st.text_input(f"Entre com o texto para filtrar a coluna {column1}"))
        else:
            value1 = st.number_input(f'Entre com o valor para filtrar pela coluna {column1}', step=1, key='7.')

        column2 = st.selectbox("Selecione a segunda coluna para filtrar", columns, key='8')
        #--CHECK TO SEE COLUMN TYPE
        if dict_column[column2] == 'object':
            value2 = str(st.text_input(f"Entre com o texto para filtrar a coluna {column2}"))
        else:
            value2 = st.number_input(f'Entre com o valor para filtrar pela coluna {column2}', step=1, key='8.')

        column3 = st.selectbox('Selecione coluna para filtrar', columns, key='9')
        #--CHECK TO SEE COLUMN TYPE
        if dict_column[column3] == 'object':
            value3 = str(st.input_text(f"Entre com o texto para filtrar a coluna {column3}"))
        else:
            value3 = st.number_input(f'Entre com o valor para filtrar pela coluna {column3}', step=1, key='9.')

        column4 = st.selectbox('Selecione quarta coluna para filtrar', columns, key='0')
        #--CHECK TO SEE COLUMN TYPE
        if dict_column[column4] == 'object':
            value4 = str(st.text_input(f"Entre com o texto para filtrar a coluna {column4}"))
        else:
            value4 = st.number_input(f'Entre com o valor para filtrar pela coluna {column4}', step=1, key='0.')
        #--CALL FUNC TO FILTER DATA BASED ON FILTERS
        filtered_data = filter_data(data, column1, value1, filtros, column2=column2, value2=column2, column3=column3,\
                                    value3=value3, column4=column4, value4=value4)

    #--FUNCTION TO THE BUTTON FILTRAR
    if st.button("Filtrar"):

        st.write("Dataset Filtrado")
        st.write(filtered_data)
        st.write(f"CNPJ's encontrados: {filtered_data.shape[0]}")

        #--FUNCTION TO THE BUTTON DOWNLOAD CSV
        if st.button('Download CSV'):
            st.write('Downloading...')
            st.write('', unsafe_allow_html=True)
            filtered_data.to_csv('filtered_data.csv', index=False)
            st.write('', download='fitered_data.csv')
        # st.markdown("""
        # <a href='data:file/csv;base64,{}' download='filtered_data.csv'>Download Dados CSV</a>
        # """.format(filtered_data.to_csv(index=False).encode().decode()), unsafe_allow_html=True)

#--CALL THE APLICATION
if __name__ == "__main__":
    main()