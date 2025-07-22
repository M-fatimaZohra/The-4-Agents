from agents import Runner
from My_Agents.Math_agent import Math_Veteran

chat_history = []
while True:
    prompt = input("Chat with Math Veteran:  ")
    if prompt.strip() == "":
        break

    chat_history.append({"role": "user", "content": prompt })
    result = Runner.run_sync(Math_Veteran, chat_history)
    chat_reply = result.final_output
    print(chat_reply)
    chat_history.append({"role": "assistant", "content": chat_reply })