# Import necessary libraries
from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

# load environment variables from .env file
load_dotenv()

# set up LLM