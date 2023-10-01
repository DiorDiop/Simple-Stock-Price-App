#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import libraries
import yfinance as yf
import streamlit as st


# In[2]:


# Set the title and description of your app
st.title('Stock Price App')
st.write('A simple web app to view stock prices.')

# Create an input field for the user to enter a stock symbol
stock_symbol = st.text_input('Enter a stock symbol (e.g., AAPL):')


# In[3]:


# Check if a stock symbol has been entered
if stock_symbol:
    try:
        # Fetch stock data using yfinance
        stock_data = yf.Ticker(stock_symbol)
        
        # Get the historical data for the stock
        historical_data = stock_data.history(period="1y")

        # Display the historical data as a line chart
        st.line_chart(historical_data['Close'])

        # Display some information about the stock
        st.write('**Company Name:**', stock_data.info['longName'])
        st.write('**Current Price:**', stock_data.history(period="1d")['Close'].iloc[-1])
        st.write('**Market Cap:**', stock_data.info['marketCap'])
    except:
        st.write('Invalid stock symbol. Please enter a valid symbol.')


# In[4]:


# Add a footer or additional information
st.write('This app is for informational purposes only.')


# In[5]:


streamlit run C:\Users\Dior\anaconda3\Lib\site-packages\ipykernel_launcher.py 


# In[ ]:




