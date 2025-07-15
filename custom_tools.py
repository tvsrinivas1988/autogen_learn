import asyncio
import os
from dotenv import load_dotenv
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_core.tools import FunctionTool

load_dotenv()

api_key =  os.getenv("OPENROUTER_API_KEY")
if not api_key:
    raise ValueError("Please set the OPENROUTER API Key!!")

model_client = OpenAIChatCompletionClient(model="deepseek/deepseek-chat-v3-0324:free",
                                          base_url="https://openrouter.ai/api/v1",
                                          api_key=os.getenv("OPENROUTER_API_KEY"),
                                          model_info={
        "family":'deepseek',
        "vision" :True,
        "function_calling":True,
        "json_output": False,
        "structured_output": False
    }
)

async def reverse_str(text:str) -> str :
    '''
    Reverse the given text

    input:str

    output:str

    The reverse string is returned.
    '''
    return text[::-1]

reverse_string_tool  = FunctionTool(reverse_str,description="Reverse  a String")

agent = AssistantAgent(
    name="ReverseStringAgent",
    model_client= model_client,
    system_message='You are a helpful assistant that can reverse string using reverse_str tool. Give the result with summary',
    tools=[reverse_str],
    reflect_on_tool_use=False
)

async def main(): 
    result = await agent.run(task = 'Reverse the string "Srinivas"')

    print(result.messages[-1].content)

if (__name__ == "__main__"):
    asyncio.run(main())