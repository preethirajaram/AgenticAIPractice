import asyncio
import os
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient

os.environ[
    "OPENAI_API_KEY"] = "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"


async def main():
    model_client = OpenAIChatCompletionClient(model="gpt-4o")
    agent = AssistantAgent(name="assistant", model_client= model_client)
    await Console(agent.run_stream(task="What is the 50*3?"))
    await model_client.close()

asyncio.run(main())