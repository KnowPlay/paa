# Import necessary libraries
from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

# load environment variables from .env file
load_dotenv()

# set up llm 
# llm = ChatOpenAI(model="gpt-4o-mini")
llm2 = ChatAnthropic(model="claude-3-5-sonnet-20241022")

# api key

