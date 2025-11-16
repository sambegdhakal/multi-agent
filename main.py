from dotenv import load_dotenv
from crew_main import stock_market_crew

load_dotenv()

def run(stock_symbol: str):
    result = stock_market_crew.kickoff(inputs={"stock": stock_symbol})
    print(result)

if __name__ == "__main__":
    run("TSLA")
