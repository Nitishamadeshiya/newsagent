from crewai import Crew, Process
from tasks import researchTask, writingTask
from agents import newsResearcher, newsWriter

#Forming the tech focused crew with some enhanced configuration

crew=Crew(
    agents=[newsResearcher, newsWriter],
    tasks=[researchTask, writingTask],
    process=Process.sequential,
)

#starting the tasks
result=crew.kickoff(inputs={'topic': 'Artificial Intelligence'})
print(result)
