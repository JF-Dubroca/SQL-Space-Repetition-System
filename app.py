import streamlit as st
import pandas as pd
import duckdb


st.write('SQL Space Repetition System')

with st.sidebar:
    option = st.selectbox(
        'What would you like to review?',
        ['Joins', 'Group By', 'Windows Functions'],
        index = None,
        placeholder='Select à theme',
    )

    st.write('You selected:', option)


data = {"a": [1, 2, 3], "b": [4, 5, 6]}
df = pd.DataFrame(data)

(tab1,) = st.tabs(["table"])
with tab1:
    sql_query = st.text_area(label="Entrez votre input")
    result = duckdb.query(sql_query).df()
    st.write(f'Votre requête: {sql_query}')
    st.dataframe(result)