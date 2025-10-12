import asyncio
import os
from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient

os.environ[
    "OPENAI_API_KEY"] = ""

async def main():
    modal_client = OpenAIChatCompletionClient(model="gpt-4o")
    RiddleAgent = AssistantAgent(name="assistant", model_client=modal_client,
                                 system_message="You need to answer the riddle question."
                                 "When the user says 'THANKS DONE' or similar, acknowledge and say 'ALL GOOD' to end session.")

    UserAgent = UserProxyAgent(name="Toddler")

    chat = RoundRobinGroupChat(participants=[UserAgent,RiddleAgent],termination_condition=TextMentionTermination("Thank you"))
    await Console(chat.run_stream(task="I need to answer the riddle question asked by user"))

    await modal_client.close()


asyncio.run(main())