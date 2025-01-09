from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
## api key setup
from dotenv import load_dotenv
## this function expect .env file
load_dotenv()

agent=Agent(

    model=Groq(id="llama-3.3-70b-versatile"),
    ## to get the latest information we need to use tool and tolls can be multiple so we need to use array  
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True),],
    ##show tools call it show api call
    show_tool_calls=True,
    ##markdown - means don't want see any special charachetrs 
    markdown=True,
    instructions=["Use Tables to display data"],
    debug_mode=True
)
 
agent.print_response("Summarize  and compare analyst recommendation and fundamentals for HDFCBank and ICICI BANK")
