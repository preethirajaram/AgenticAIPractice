import asyncio
import json
import os

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient

os.environ["OPENAI_API_KEY"] = ""

async def main():

    model_client = OpenAIChatCompletionClient(api_key=os.environ["OPENAI_API_KEY"],model="gpt-4o")

    agent1 = AssistantAgent(name="Agent1", model_client=model_client)

    await Console(agent1.run_stream(task="My favourite country is Australia"))

    agent2 = AssistantAgent(name="Agent2", model_client=model_client)

    state = await agent1.save_state()

    with open("state.json", "w") as f:
        json.dump(state, f,default=str)

    with open("state.json", "r") as f:
        stateSaved = json.load(f)

    await agent2.load_state(stateSaved)

    await Console(agent2.run_stream(task="what is my favourite country?"))

    await model_client.close()



asyncio.run(main())