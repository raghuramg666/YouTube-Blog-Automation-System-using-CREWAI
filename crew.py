from crewai import Crew,Process
from agents import blog_researcher,blog_writer
from task import research_task,write_task


#formign  the tech-focused crew with some enhanced configurations

crew=Crew(
agents=[blog_researcher,blog_writer],
tasks=[research_task,write_task],
process=Process.sequential,
memory=True,
cache=True,
max_rpm=100,
share_crew=True


)


##startm task execution proces with enhanced feedback
result=crew.kickoff(inputs={'topic':'AI vs ML vs DL vs Data Science'})
print(result)