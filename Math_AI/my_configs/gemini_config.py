from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import OpenAIChatCompletionsModel, set_tracing_disabled
import os

set_tracing_disabled (True) #hide OPENAI_API_KEY is not set, skipping trace export
load_dotenv(override=True) #Forces .env values to replace existing environment variables.

my_gemini_key = os.getenv("GEMINI_API_KEY") #fetch api key from .env
CLIENT = AsyncOpenAI(api_key=my_gemini_key, base_url="https://generativelanguage.googleapis.com/v1beta/openai/") #it is a class that take apikey of LLM and and endpoint for model access
MODEL = OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=CLIENT) #Model created for Agents Activation, it expicitly give model name-version and client from above line to get model 


#cofiguration  completed