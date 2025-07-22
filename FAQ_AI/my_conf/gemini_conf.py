from dotenv import load_dotenv 
from openai import AsyncOpenAI
from agents import OpenAIChatCompletionsModel, set_tracing_disabled
import os


set_tracing_disabled(True)

load_dotenv(override=True)
my_key = os.getenv("GEMINI_API_KEY")
CLIENT = AsyncOpenAI(api_key=my_key,base_url="https://generativelanguage.googleapis.com/v1beta/openai/")
MODEL = OpenAIChatCompletionsModel(model="gemini-2.0-flash",openai_client=CLIENT)




