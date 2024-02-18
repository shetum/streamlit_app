import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import plotly.graph_objects as go

st.title("Название сайта")

df = pd.read_excel("my_data.xlsx")
df1 = pd.DataFrame(df)
st.write("""
# Мой первый дашборд
Представленные данные *вымышленные!*
""")

start_d, end_d = st.select_slider(
    'Выбираем интервал: ',
    options=[int(i) for i in range(2001,2021,1)],
    value=(2001, 2020))

fig = px.line(df.iloc[start_d - 2000:end_d-1999], x= "Year", y = ["Sebes","Price","Volume"])
st.plotly_chart(fig)


col1, col2 = st.columns(2)
col1.metric("Себестоимость", f"{df.iloc[end_d - 2001]['Sebes']} руб.", f"{round((df.iloc[end_d-2001]['Sebes']/df.iloc[start_d - 2000]['Sebes'] - 1) * 100, 2)} %")
col2.metric("Стоимость", f"{df.iloc[end_d - 2001]['Price']} руб.", f"{round((df.iloc[end_d-2001]['Price']/df.iloc[start_d - 2000]['Price'] - 1) * 100, 2)} %")

col3, col4 = st.columns(2)
col3.metric(f"С1 {start_d} год", f"{round(((df.iloc[start_d-2000]['Price']-df.iloc[start_d - 2000]['Sebes'])/df.iloc[start_d - 2000]['Price'])  * 100, 2)}%")
col4.metric(f"С1 {end_d} год", f"{round((((df.iloc[end_d-2001]['Price']-df.iloc[end_d - 2001]['Sebes'])/df.iloc[end_d-2001]['Price']) * 100), 2)}%")
col5, col6, col7 = st.columns(3)
col6.metric("Объём",f"{df.iloc[end_d - 2001]['Volume']} шт.", f"{round((df.iloc[end_d-2001]['Volume']/df.iloc[start_d - 2000]['Volume'] - 1) * 100, 2)} %" )
#col5 = st.columns(1)
#col5.metric("Разница")
#col5.metric(delta = round((((df.iloc[end_d-2001]['Price']-df.iloc[end_d - 2001]['Sebes'])/df.iloc[end_d-2001]['Price']) * 100) - ((df.iloc[start_d-2001]['Price']-df.iloc[start_d - 2001]['Sebes'])/df.iloc[start_d - 2001]['Price'])  * 100, 2))

def sun():
    data = pd.read_excel("sunburst.xlsx")
    df = pd.DataFrame(data = data)

    fig = px.sunburst(df,
                    path= ["GAU","NOM"],
                    values = "Sebes",
                    title = "Себестоимость ГП SOLVIS",
                    width=500, height=500)
    st.plotly_chart(fig)

status = st.radio("Выберете страну: ", ("Италия" , "Германия", "Россия"))

if status == "Россия":
    st.success("Россия")
else:
    st.warning("Не Россия")
    