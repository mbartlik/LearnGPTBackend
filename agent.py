# from langchain.llms import OpenAI
# from langchain.tools import Tool
# from langchain.agents import AgentType, initialize_agent
# from dotenv import dotenv_values

# config = dotenv_values(".env")
# api_key = config["openai_key"]
# llm = OpenAI(openai_api_key=api_key, temperature=0)

# def tool_func(object_type):
#     print("$$$$$")
#     print(object_type)
#     if object_type is "bumblebee":
#         return "purple"
#     if object_type is "sky":
#         return "green"
#     return "red"
# tools = [
#     Tool.from_function(
#         func=tool_func,
#         name = "Colors",
#         description="can tell you the color of something. As parameters you will give the thing, in all lowercase."
#         # coroutine= ... <- you can specify an async method if desired as well
#     ),
# ]

# agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)