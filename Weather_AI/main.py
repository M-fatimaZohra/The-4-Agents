from agents import Runner
from My_Agents.Weather_Agent import Weather_agent


chat_history = []
while True:
    prompt = input(f"Chat with weather ai :  ")
    if prompt.strip() == "":
        break

    chat_history.append({"role": "user", "content": prompt })
    result = Runner.run_sync(Weather_agent, chat_history)
    chat_reply = result.final_output
    print(chat_reply)
    chat_history.append({"role": "assistant", "content": chat_reply })