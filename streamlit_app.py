import streamlit as st
import pandas as pd
st.set_page_config(layout='wide', page_title='Sentiment vs PnL')
st.title('Sentiment vs Trader Performance — Demo')
trades = pd.read_csv('submission_package/trades_clean.csv', parse_dates=['time'])
sent = pd.read_csv('submission_package/sentiment_clean.csv', parse_dates=['date'])
st.sidebar.header('Filters')
acct = st.sidebar.selectbox('Account', ['ALL'] + sorted(trades['account'].dropna().unique().tolist()))
if acct != 'ALL':
    trades = trades[trades['account']==acct]
st.write('Trades head:')
st.dataframe(trades.head())
st.write('Sentiment head:')
st.dataframe(sent.head())