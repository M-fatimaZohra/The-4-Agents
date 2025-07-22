from agents import Agent
from my_configs.gemini_config import MODEL
from Tools.basic_addition import addition

agent_name = "Math Veteran"
Math_Veteran = Agent(name=agent_name,
                     instructions=f"your name is {agent_name} expert in Math equations, operations and expression but \
                                    -if some ask for two number addition operation use given tool addition.\
                                    -use correct formatting and sequence, use code formatting box if necessary\
                                    -Refuse to answer any question politely if someone asks questions that are non-math related",
                     model=MODEL,
                     tools=[addition],
                     tool_use_behavior="run_llm_again" #this will make enchantment on tool and rewrite answer, while stop_on_first_tool will give tool's hardcode answer

                     )
