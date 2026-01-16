# pylint: disable = missing-module-docstring
import io

import duckdb
import pandas as pd
import streamlit as st

CSV = """
beverage,price
orange juice,2.5
Expresso,2
Tea,3
"""
beverages = pd.read_csv(io.StringIO(CSV))

CSV2 = """
food_items,food_price
cookie,3.5
chocolatine,2
muffin,3
"""

food_items = pd.read_csv(io.StringIO(CSV2))

ANSWER = """
SELECT * FROM beverages
CROSS JOIN food_items
"""

solution = duckdb.sql(ANSWER).df()

st.write("SQL Space Repetition System pratice")

with st.sidebar:
    option = st.selectbox(
        "What would you like to review?",
        ["Joins", "Group By", "Windows Functions"],
        index=None,
        placeholder="Select à theme",
    )

    st.write("You selected:", option)

st.header("Entrez votre code")
query = st.text_area(label="Votre code SQL ici", key="user_input")

if query:
    result = duckdb.sql(query).df()
    st.dataframe(result)

    # Vérification du nombre de ligne et du nombre de colonnes
    nb_solution_lines = solution.shape[0]
    nb_solution_columns = solution.shape[1]
    nb_result_lines = result.shape[0]
    nb_result_columns = result.shape[1]

    if nb_result_lines != nb_solution_lines:
        st.write("Le nombre de lignes est incorrect")

    if nb_result_columns != nb_solution_columns:
        st.write("Le nombre de colonnes est incorrest")

    if (
        nb_result_columns == nb_solution_columns
        and nb_result_lines == nb_solution_lines
    ):
        st.write("Bravo, tu as trouvé la solution")

    try:
        result = result[solution.columns]
        st.dataframe(result.compare(solution))
    except KeyError as e:
        st.write("Ce n'est pas le bon résultat")

tab2, tab3 = st.tabs(["Table", "Solution"])

with tab2:
    st.write("Table: beverages")
    st.dataframe(beverages)
    st.write("Table: food_items")
    st.dataframe(food_items)
    st.write("Expected")
    st.dataframe(solution)

with tab3:
    st.write(ANSWER)
