import asyncio

import os
from _pyrepl.console import Console
from itertools import count

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_agentchat.conditions import MaxMessageTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_ext.models.openai import OpenAIChatCompletionClient

os.environ[
    "OPENAI_API_KEY"] = "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"



async def main():
    model_client = OpenAIChatCompletionClient(model="gpt-4o")
    agent1 = AssistantAgent(name="StudentAgent", model_client= model_client,
                            system_message="Your are a student Agent who wants to know "
                                           "how to learn multiplication tables and practice steps to excel in maths"
                                           "as your in grade 2")

    agent2 = AssistantAgent(name="TeacherAgent", model_client= model_client,
                            system_message="Your are a Teacher Agent who should provide information "
                                           " to the StudentAgent")\

    team = RoundRobinGroupChat(participants=[agent2, agent1],termination_condition=MaxMessageTermination( max_messages=3))

    await Console(team.run_stream(task="Hello, wanted to know more about multiplication tables?"))
    await model_client.close()


asyncio.run(main())