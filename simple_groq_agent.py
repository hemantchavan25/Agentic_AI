from phi.agent import Agent
from phi.model.groq import Groq
## api key setup
from dotenv import load_dotenv
## this function expect .env file
load_dotenv()

agent=Agent(
    model=Groq(id="llama-3.3-70b-versatile")
)

agent.print_response("correct the sentense Who sits next at you in class")
