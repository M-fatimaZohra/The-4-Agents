from openai import AsyncOpenAI
from dotenv import load_dotenv
from agents import OpenAIChatCompletionsModel, set_tracing_disabled, RunConfig
import os

set_tracing_disabled(True)
load_dotenv(override=True)

key = os.getenv("GEMINI_API_KEY")
BASE_URL ="https://generativelanguage.googleapis.com/v1beta/openai/"
CLIENT = AsyncOpenAI(api_key=key,base_url=BASE_URL)
MODEL = OpenAIChatCompletionsModel(model="gemini-2.0-flash",openai_client=CLIENT)


# RunConfig(
#     model=MODEL,
#     model_provider= CLIENT,
#     tracing_disabled= True
    
# )

