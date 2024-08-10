import streamlit as st
import click
from crewai import Agent, Task, Crew
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.llms import Ollama
from crewai_tools import tool
from langchain.chains import  LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains import  RetrievalQA
from langchain.document_loaders import  TextLoader
from langchain.embeddings import  OpenAIEmbeddings
from langchain.vectorstores import  FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.memory import ConversationBufferMemory
from langchain.chains import  ConversationalRetrievalChain
import time
from tqdm import tqdm

# --- Configuration ---

# Model Name (Replace with your chosen Ollama model)
model_name = "internal-m2"

# Research Topic
research_topic = "Automated passive income generating from home online crypto income solution"

# --- Functions ---

@tool("Duck_Duck_Go_Search")
def ddgsearch(question: str) -> str:
    """Searches DuckDuckGo for information."""
    return DuckDuckGoSearchRun().run(question)

# --- Agents ---

researcher = Agent(
    role='Researcher',
    goal=f'Research and develop a six-figure income-producing automated passive income solution focused on crypto, generating from home online.',
    backstory="""
    You are an expert financial researcher and developer specializing in cryptocurrency. 
    You are tasked with researching and designing an automated passive income system using crypto.
    Your goal is to find and analyze existing solutions, identify opportunities, and generate specific steps for implementation.
    Focus on scalability, security, and long-term sustainability.
    """,
    verbose=True,            
    allow_delegation=False,  
    tools=[ddgsearch],        
    llm=Ollama(model=model_name)  
)

writer = Agent(
    role='Tech Content Strategist',
    goal='Craft a detailed plan outlining the steps and resources needed to implement the researched crypto income solution.',
    backstory="""
    You are a skilled technical writer with a deep understanding of cryptocurrency and online business. 
    Your role is to translate complex research findings into a clear and actionable plan.
    Break down the solution into manageable steps, provide resources for each step, and ensure the plan is easily understood by a beginner. 
    """,
    verbose=True,            
    allow_delegation=True,   
    llm=Ollama(model=model_name)  
)

# --- Tasks ---

task1 = Task(
    agent=researcher,
    description=research_topic,
    expected_output="A comprehensive report outlining the steps and resources required to develop a six-figure crypto passive income solution, ensuring scalability, security, and long-term sustainability."
)

task2 = Task(
    agent=writer,
    description="""
    Using the insights provided by the researcher, create a detailed implementation plan for the crypto income solution.
    The plan should include the following:
      - A clear step-by-step guide for setting up the solution.
      - Specific resources, tools, and platforms needed for each step.
      - Potential challenges and mitigation strategies.
      - Strategies for ongoing maintenance and optimization.
    The plan should be comprehensive and easy to understand, targeting beginners with minimal technical experience.
    """,
    expected_output="""A detailed implementation plan for the crypto income solution, broken down into manageable steps, with specific resources and tools provided for each step. The plan should be easy to follow and suitable for beginners."""
)

# --- Crew ---

crew = Crew(
    agents=[researcher, writer],
    tasks=[task1, task2],
    verbose=2 
)

# --- Execution ---

def run_agents(research_topic):
    """Runs the agents and tasks with progress tracking."""
    with tqdm(total=100, desc="Skyscope Sentinel: Generating Solution", bar_format='{desc}:{percentage:3.0f}%|{bar}| {n_fmt}/{total_fmt}') as pbar:
        result = crew.kickoff()
        pbar.update(50)  # Update progress bar

        # --- Process output with more detail ---
        click.echo("\n****************************************")
        click.echo(f"Skyscope Sentinel Multi Agent AI Entrepreneur - Crypto Income Solution")
        click.echo("****************************************")

        click.echo("\n\nResearch Report:")
        click.echo(result[0].output)

        click.echo("\n\nImplementation Plan:")
        click.echo(result[1].output)
        
        pbar.update(50)  # Update progress bar

# --- Streamlit WebUI ---

def streamlit_app():
    """Defines the Streamlit Web UI."""
    st.title("Skyscope Sentinel Multi Agent AI Entrepreneur")
    st.markdown("Developed by: Casey J Topojani")
    st.markdown("License: MIT")

    # Input for the research topic
    research_topic = st.text_input("Enter your research topic:", "Automated passive income generating from home online crypto income solution")

    if st.button("Generate Solution"):
        run_agents(research_topic)  # Run the agents with progress bar

# --- Click CLI ---

@click.command()
@click.option('--topic', prompt="Enter your research topic", default="Automated passive income generating from home online crypto income solution")
def cli_app(topic):
    """Defines the Click CLI."""
    click.echo("Skyscope Sentinel Multi Agent AI Entrepreneur")
    click.echo("Developed by: Casey J Topojani")
    click.echo("License: MIT")

    run_agents(topic)  # Run the agents with progress bar

# --- Run the app ---

if __name__ == '__main__':
    if st. __name__ == '__main__':
        streamlit_app()
    else:
        cli_app()
