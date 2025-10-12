import asyncio
import os

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.messages import MultiModalMessage
from autogen_agentchat.ui import Console
from autogen_core import Image
from autogen_ext.models.openai import OpenAIChatCompletionClient

os.environ[
    "OPENAI_API_KEY"] = ""


async def main():

    model_client = OpenAIChatCompletionClient(model="gpt-4o")
    assistant = AssistantAgent(name="MultiModalAgent", model_client=model_client)
    image = Image.from_file("/Users/rajarammanoharan/Downloads/Statista.jpeg")
    multimodalmsg = MultiModalMessage(content=["What do you see in this graph image",image],source="user")

    await Console(assistant.run_stream(task=multimodalmsg))
    await model_client.close()


asyncio.run(main())