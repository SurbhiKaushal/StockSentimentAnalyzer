import yfinance as yf
def get_stock_data(symbol):
    """
    Fetch recent stock data for a given symbol.
    """
    try:
        data = yf.download(symbol, period="7d", interval="1h")
        return data
    except Exception as e:
        print("Error fetching stock data:", e)
        return None
