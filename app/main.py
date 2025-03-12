import os
from crewai import Agent, Task, Crew, Process
from openai import OpenAI
# from dotenv import load_dotenv

# # Load environment variables from a specific path
# load_dotenv(dotenv_path='../.env')

# Load API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("Missing OpenAI API Key")

# Define Agents
researcher = Agent(
    name="Researcher",
    role="AI Research Analyst",
    goal="Gather relevant information on a topic",
    backstory="A seasoned analyst specializing in AI research and data collection.",
    llm=OpenAI(api_key=OPENAI_API_KEY)
)

documenter = Agent(
    name="Documenter",
    role="Technical Writer",
    goal="Summarize research into a structured document",
    backstory="An expert in converting research into concise reports.",
    llm=OpenAI(api_key=OPENAI_API_KEY)
)

# Define Tasks
research_task = Task(
    description="Find the latest advancements in AI research.",
    agent=researcher
)

document_task = Task(
    description="Write a structured document based on research findings.",
    agent=documenter,
    depends_on=[research_task]
)

# Define Crew
crew = Crew(
    agents=[researcher, documenter],
    tasks=[research_task, document_task],
    process=Process.sequential
)

def main():
    result = crew.kickoff()
    print("Final Output:", result)

if __name__ == "__main__":
    main()
