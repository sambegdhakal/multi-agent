from crewai import Task
from agents.analyst_agent import analyst_agent

get_stock_analysis = Task(
    description=(
        "Analyze performance of the stock: {stock} based on current and past 7 days data. Use the live stock information tool to retrieve"
        "Provide the summary of how the stock is performing"),

    expected_output = (
        "bullet pointed summary of Current stock price, price change and percentage over the time period, volume and volatility, "
        "and Any immediate trends or observations with two line explanation"
        "All of these in proper points"
    ),
    agent=analyst_agent

)