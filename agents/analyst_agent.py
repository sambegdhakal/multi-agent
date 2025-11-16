from crewai import Agent, LLM

from tools.stock_research_tool import get_stock_price

#first initialize LLMs
llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    temperature=0.0
)

analyst_agent = Agent(
    role="Financial Market Analyst",
    goal=("Perform in depth analysis of publicly traded stock."
        "Idemtify trends, performance, financial signals for stock investment and sell"),
    backstory= ("Expert financial analyst with deep expertise in interpreting stock data and"
                "also specializes in producing well-structured reports for investment and selling opportunities using current and past data."),
    llm=llm,
    tools=[get_stock_price],
    verbose=True
)