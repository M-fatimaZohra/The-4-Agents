from agents import Runner
from My_Agents.multi_service_agent import Lunna_AI

chat_history = []
while True:
    prompt = input("Chat with Lunna AI:  ")
    if prompt.strip() == "":
        break

    chat_history.append({"role": "user", "content": prompt })
    result = Runner.run_sync(Lunna_AI, chat_history)  # Run the agent with the chat history
    chat_reply = result.final_output
    print(chat_reply)
    chat_history.append({"role": "assistant", "content": chat_reply })