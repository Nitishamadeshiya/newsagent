from crewai import Agent, LLM
from tools import tool
import os
from dotenv import load_dotenv
load_dotenv()

llm = LLM(
    model="gemini-2.5-flash",
    provider="google",
    api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.7,
)

# Creating a senior researcher agent
newsResearcher=Agent(
    role="Senior Researcher",
    goal='Uncover ground breaking technologies in {topic} and provide a comprehensive report.',
    verbose=True,
    memory=True,
    backstory="You are a senior researcher with expertise in technology trends and innovations. Your task is to investigate and analyze the latest advancements in the field of {topic}. You will gather information from various sources, evaluate the significance of the findings, and compile a detailed report that highlights the most promising technologies and their potential impact on the industry.",
    tools=[tool],
    llm=llm,
    allow_delegation=True
    
)


# creating a write agent with custom tools responsible for writing the report

newsWriter=Agent(

    role="Writer",
    goal='Write a comprehensive report on the latest advancements in {topic} based on the research findings provided by the Senior Researcher.',
    verbose=True,
    memory=True,
    backstory="You are a skilled writer with expertise in crafting detailed and informative reports. Your task is to take the research findings provided by the Senior Researcher and transform them into a well-structured and engaging report. You will organize the information, highlight key insights, and present the findings in a clear and concise manner that is accessible to a wide audience.",
    tools=[tool],
    llm=llm,
    allow_delegation=False
)

