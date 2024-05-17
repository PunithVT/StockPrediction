import streamlit as st
from plotly import graph_objects as go
from datetime import date
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly

START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.title("Stock Prediction And Analysis")

stocks = ('GOOG', 'AAPL', 'MSFT', 'GME')
# User input for custom stock
user_input_stock = st.text_input('Enter a stock symbol (optional):')

# Combine predefined and user input (if any)
all_stocks = list(stocks)  # Convert tuple to list for modification
if user_input_stock:
  all_stocks.insert(0, user_input_stock.upper()) # Convert user input to uppercase

selected_stock = st.selectbox("Select the Stock to prediction", all_stocks)

nYear = st.slider("Years of Prediction",1,5)
period = nYear*365

#@st.cache
def loadData(ticker):
  data = yf.download(ticker,START,TODAY)
  return data
#data=loadData(selected_stock)

with st.status("Downloading data..."):
    data=loadData(selected_stock)
    data.reset_index(inplace=True)
    st.write("Downloaded")

st.subheader("Sample Data")
st.write(data.tail())

def plotSampleData():
   fig = go.Figure()
   fig.add_trace(go.Scatter(x=data['Date'],y=data['Open'],name="Stock Open"))
   fig.add_trace(go.Scatter(x=data['Date'],y=data['Close'],name="Stock Close"))
   fig.layout.update(xaxis_rangeslider_visible=True)
   st.plotly_chart(fig)
plotSampleData()

# Predict forecast with Prophet.
df_train = data[['Date','Close']]
df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

m = Prophet()
m.fit(df_train)
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)

# Show and plot forecast
st.subheader('Forecast data')
st.write(forecast.tail())
    
st.write(f'Forecast plot for {nYear} years')
fig1 = plot_plotly(m, forecast)
st.plotly_chart(fig1)

st.write("Forecast components")
fig2 = m.plot_components(forecast)
st.write(fig2)



