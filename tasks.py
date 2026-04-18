from crewai import Task
from tools import tool
from agents import newsResearcher, newsWriter

# Research task
researchTask=Task(
    description=("Identify the next big trend in {topic}."
    "Focus on identifying pros ans cons and the overall narrative."),
    expected_output="A comprehensive report detailing the next big trend in {topic}, including its potential impact, advantages, disadvantages, and the overall narrative surrounding it.",
    tools=[tool],
    agent=newsResearcher,
    )

#Writing task
writingTask=Task(
    description="Write a comprehensive report on the next big trend in {topic} based on the research findings provided by the Senior Researcher.",
    expected_output="A well-structured and engaging report that presents the research findings on the next big trend in {topic} in a clear and concise manner.",
    tools=[tool],
    agent=newsWriter,
    async_execution=False,
    output_file='new_blog_post.md'
)

