import streamlit as st
import pandas as pd
from stock_data import get_stock_data
from sentiment_analysis import analyze_sentiment
import matplotlib.pyplot as plt
st.set_page_config(page_title="Stock Sentiment Analyzer", page_icon="📈")
st.title("📈 Stock Sentiment Analyzer")
st.write("Analyze stock trends and public sentiment for your favorite companies.")
symbol = st.text_input("Enter Stock Symbol (e.g. AAPL, TSLA, INFY, TCS):", "AAPL")
sample_headlines = [
    f"{symbol} stock hits record high amid strong earnings.",
    f"Analysts warn {symbol} may face competition soon.",
    f"Investors remain optimistic about {symbol}'s growth.",
    f"{symbol} shares tumble due to market uncertainty.",
    f"{symbol} announces new product line."
]
if st.button("Analyze"):
    data = get_stock_data(symbol)
    if data is not None and not data.empty:
        st.subheader(f"📊 Stock Price Trend for {symbol}")
        st.line_chart(data['Close'])
    else:
        st.warning("Unable to fetch stock data. Try a valid symbol (like AAPL, TSLA, TCS).")
    st.subheader("🧠 Sentiment Analysis from Headlines")
    sentiment_results = []
    for headline in sample_headlines:
        result = analyze_sentiment(headline)
        sentiment_results.append({"Headline": headline, "Sentiment": result})
    df = pd.DataFrame(sentiment_results)
    st.table(df)
    positive = len(df[df['Sentiment'].str.contains('Positive')])
    negative = len(df[df['Sentiment'].str.contains('Negative')])
    neutral = len(df[df['Sentiment'].str.contains('Neutral')])
    st.subheader("📉 Sentiment Summary")
    fig, ax = plt.subplots()
    ax.bar(["Positive", "Neutral", "Negative"], [positive, neutral, negative])
    st.pyplot(fig)
st.markdown("---")
st.markdown("Built with using Python, Streamlit, and VADER Sentiment Analysis.")
