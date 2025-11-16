import yfinance as yf
from crewai.tools import tool

@tool("Live Stock Information Tool")
def get_stock_price(stock_symbol: str) -> str:
    """
    retrieving latest stock price
    """
    stock =yf.Ticker(stock_symbol)
    info = stock.info

    hist = stock.history(period="7d")

    current_price = info.get("regularMarketPrice")
    change = info.get("regularMarketChange")
    change_percent = info.get("regularMarketChangePercent")
    currency = info.get("currency", "USD")

    if current_price is None:
        return f"Data missing for {stock_symbol}"

    return {
        "symbol": stock_symbol,
        "current": {
            "price": current_price,
            "change": change,
            "change_percent": round(change_percent, 2) if change_percent else None,
            "currency": currency
        },
        "past_7_days": hist.reset_index().to_dict(orient="records")
    }
