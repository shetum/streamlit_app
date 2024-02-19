import streamlit as st
from datetime import date

import yfinance as yf

from plotly import graph_objs as go

START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.title("Цены на акции")

stocks = ('GOOG', 'AAPL', 'MSFT', 'GME','TSLA','AMZN','NVDA',)
selected_stock =st.selectbox("Выбери акцию", stocks)

intervals = ('1d', '5d', '1mo', '3mo')
selected_intervals =st.selectbox("Выбери фрейм", intervals)


#@st.cache_data 
def load_data(ticker):
    data = yf.download(ticker, START, TODAY, interval = selected_intervals)
    data.reset_index(inplace = True)
    return data

data_load_state = st.info("Данные загружаются")
data = load_data(selected_stock)
data_load_state.success("Данные загружены")



def plot_raw_data_candle(color1, color2):
    fig = go.Figure(data=[go.Candlestick(x=data['Date'],
                open=data['Open'],
                high=data['High'],
                low=data['Low'],
                close=data['Close'], increasing_line_color= color1, decreasing_line_color= color2)])
    fig.layout.update(title_text= f'График цены {selected_stock}', xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

def plot_raw_data():
	fig = go.Figure()
	fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock_open"))
	fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close"))
	fig.layout.update(title_text= f'График цены {selected_stock}', xaxis_rangeslider_visible=True)
	st.plotly_chart(fig)

type_if_fig = ('candle', 'line')
selected_type_stock =st.selectbox("Выбери тип графика", type_if_fig)

color1 = st.color_picker("Первый цвет", "#00FF23", label_visibility="visible")
color2 = st.color_picker("Второй цвет","#FF0000",label_visibility="visible")

if selected_type_stock == "candle":
    plot_raw_data_candle(color1 = color1, color2 = color2)
else:
    plot_raw_data()



from st_pages import Page, show_pages, add_page_title

# Optional -- adds the title and icon to the current page
add_page_title()

# Specify what pages should be shown in the sidebar, and what their titles and icons
# should be
show_pages(
    [
        Page("main.py", "Stock price", "🏠"),
        Page("gambling.py", "Gambling", "🏠"),
    ]
)


