# импортируем библиотеку streamlit
import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt

st.write('За основу я взял базу данных...')
if st.button("узнать"):
    st.write("..о пассажирах Титаника")

st.divider()

st.title("Таблица пассажиров")

df = pd.read_csv("titanic.csv")
st.write(df)

st.caption("Это мой последний контрол в этой работе")
