from crewai import Agent 
from tools import yt_tool
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
import os
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"]="gpt-4-0125-preview"
llm=OpenAI()

##Create a senior blog content researcher
blog_researcher=Agent(
    role='Blog Researcher from youtube videos',
    goal='get the relevant content for the topic {topic} from YT channel',
    verbose=True,
    memory=True,
    backstory=(
        "Expert in understanding videos in AI Data Science, MAchine LEarning and Gen AI and providing suggestions"
    ),
    tools=[yt_tool],
    allow_delegation=True


)


##Create agent for a senior blog writer agent with YT Tool

blog_writer=Agent(
role='Blog Writer',
goal='Narrate compelling tech stories about the vidoe {topic} from Yt channel',
verbose=True,
memory=True,
backstory=(
    "with a flair for simplifying complex topics, you craft"
    "engaging narratives that captivate and educate , bringing new"
    "discoveries to light in an accessible manner"

),
tools=[yt_tool],
llm=llm,

allow_delegation=False

)