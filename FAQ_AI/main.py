import asyncio
from agents import Runner
from my_Agents.agent_00 import FAQ




chat_history = []
while True:
    input_prompt = input("ASk Questions to FAQ AI: ")
    if input_prompt.strip() == "":
          break
    chat_history.append({"role": "user", "content": input_prompt })
    async def main():
            result = await Runner.run(FAQ, chat_history)
            print(result.final_output)
            chat_history.append({"role": "assistant", "content": result.final_output})


    asyncio.run(main()) 
     