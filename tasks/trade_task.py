from crewai import Task
from agents.trader_agent import trader_agent

trade_decision = Task(
    description=(
        "Use live market data and stock performance indicators for {stock} to make a strategic trading decision. "
        "Assess all key factors to make that decision."
        "Based on the analysis, recommend whether to buy, sale or hold the stock"),

    expected_output = (
        "A clear and confident trading recommendation to either Buy, sell or Hold."
        "Support your reasons with current stock price and daily change, volume and market activity and "
        "also justification for trading based on technical signals or  risk-reward"

    ),
    agent=trader_agent

)