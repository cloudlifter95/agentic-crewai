import os
import time
from tqdm import tqdm
from crewai import Agent, Task, Crew, LLM
from dotenv import load_dotenv

# # Load environment variables from a specific path
# load_dotenv(dotenv_path='config/.env')
# Load API Key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("Missing API Key")


def rate_limit_delay(delay=70):
    print(f"Sleeping for {delay} seconds to avoid throttling of LLM API ...")
    for _ in tqdm(range(delay), desc="Waiting", unit="sec"):
        time.sleep(1)  # Sleep in 1-second intervals for smooth progress


# Initialize Large Language Model (LLM) of your choice (see all models on our Models page)
llm = LLM(model="groq/llama-3.3-70b-versatile")

# Create your CrewAI agents with role, main goal/objective, and backstory/personality
summarizer = Agent(
    role='Documentation Summarizer',  # Agent's job title/function
    goal='Create concise summaries of technical documentation',  # Agent's main objective
    # Agent's background/expertise
    backstory='Technical writer who excels at simplifying complex concepts',
    llm=llm,  # LLM that powers your agent
    verbose=True  # Show agent's thought process as it completes its task
)

translator = Agent(
    role='Technical Translator',
    goal='Translate technical documentation to other languages',
    backstory='Technical translator specializing in software documentation',
    llm=llm,
    verbose=True
)

quality_assurance_agent = Agent(
    role='Quality Assurance Agent',
    goal='Proofreads the technical translation from the technical translator.',
    backstory='Seasoned Technical translator who has transitioned to Quality assurance.',
    llm=llm,
    allow_delegation=True,
    verbose=True
)

# Define your agents' tasks
summary_task = Task(
    description='Summarize this React hook documentation:\n\nuseFetch(url) is a custom hook for making HTTP requests. It returns { data, loading, error } and automatically handles loading states.',
    expected_output="A clear, concise summary of the hook's functionality",
    agent=summarizer  # Agent assigned to task
)

translation_task = Task(
    description='Translate the summary to French',
    expected_output="French translation of the hook documentation",
    agent=translator,
    dependencies=[summary_task]  # Must run after the summary task
)

quality_assurance_task = Task(
    description='Proofread the translation for errors and inacuracies. Keep the brand image by upholding a friendly and professional demeanor',
    expected_output="Accurate concize summary with a friendly yet professional tone",
    agent=quality_assurance_agent,
    dependencies=[translation_task]  # Must run after the summary task
)


# Create crew to manage agents and task workflow
crew = Crew(
    # Agents to include in your crew
    agents=[summarizer, translator, quality_assurance_agent],
    # Tasks in execution order
    tasks=[summary_task, translation_task, quality_assurance_task],
    verbose=True
)
rate_limit_delay()
result = crew.kickoff()
print(result)


# def main():
#     result = crew.kickoff()
#     print("Final Output:", result)

if __name__ == "__main__":
    print('Good')
    # main()
