from crewai import Crew

from tasks.trade_task import trade_decision
from tasks.analyse_task import get_stock_analysis
from agents.analyst_agent import analyst_agent
from agents.trader_agent import trader_agent

stock_market_crew= Crew(
    agents=[analyst_agent, trader_agent], #have to make sure they are in order
    tasks=[get_stock_analysis, trade_decision], # have to make sure they are in order
    verbose=True
)

