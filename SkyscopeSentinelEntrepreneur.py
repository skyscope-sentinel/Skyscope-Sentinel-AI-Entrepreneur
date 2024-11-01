import os
import subprocess
import sys
import streamlit as st
import click
from crewai import Agent, Task, Crew
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.llms import Ollama
from crewai_tools import tool
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.document_loaders import TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from tqdm import tqdm
import time

# --- Configuration ---
model_name = "internml2.5"  # Specify the Ollama model version
research_topic_default = "Automated passive income generating from home online crypto income solution"

# --- Functions ---

def check_ollama_installed():
    """Check if Ollama is installed on the system."""
    try:
        subprocess.check_call(["ollama", "--version"])
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Ollama is not installed. Please install it to proceed.")
        return False

def pull_ollama_model(model_name):
    """Ensure the specified Ollama model is available locally."""
    try:
        subprocess.check_call(["ollama", "pull", f"{model_name}:latest"])
        print(f"Model {model_name}:latest is ready for use.")
    except subprocess.CalledProcessError:
        print(f"Failed to pull {model_name}:latest. Please check your Ollama installation.")

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
    Your goal is to find and analyze existing solutions, identify opportunities, and generate specific steps for implementation.
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
    """,
    verbose=True,
    allow_delegation=True,
    llm=Ollama(model=model_name)
)

# --- Tasks ---

task1 = Task(
    agent=researcher,
    description=research_topic_default,
    expected_output="A comprehensive report on steps and resources for developing a sustainable crypto income solution."
)

task2 = Task(
    agent=writer,
    description="""
    Using the insights provided by the researcher, create a detailed implementation plan for the crypto income solution.
    """,
    expected_output="A detailed plan with steps, tools, and resources needed for beginners."
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
        pbar.update(50)

        print("\n****************************************")
        print("Skyscope Sentinel Multi-Agent AI Entrepreneur")
        print("****************************************")
        print("\nResearch Report:")
        print(result[0].output)
        print("\nImplementation Plan:")
        print(result[1].output)

        pbar.update(50)

# --- Streamlit WebUI ---

def streamlit_app():
    """Defines the Streamlit Web UI."""
    # Set Streamlit dark theme configuration
    st.set_page_config(page_title="Skyscope Sentinel AI Entrepreneur", layout="centered", initial_sidebar_state="auto")

    # Apply custom CSS for gradient and dark theme styling
    st.markdown("""
        <style>
            body {
                background-color: #1e1e1e;
                color: #ffffff;
            }
            .main-title {
                font-size: 2.5rem;
                font-weight: bold;
                background: -webkit-linear-gradient(45deg, #42a5f5, #478ed1);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                text-align: center;
            }
            .sub-title {
                font-size: 1rem;
                color: #bbdefb;
                text-align: center;
                font-weight: bold;
            }
        </style>
    """, unsafe_allow_html=True)

    # Display title with gradient effect and subtitle
    st.markdown('<h1 class="main-title">Skyscope Sentinel Entrepreneur</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">by Skyscope Sentinel Intelligence</p>', unsafe_allow_html=True)

    # Check Ollama model availability and pull if necessary
    if not check_ollama_installed():
        st.error("Ollama is not installed. Please install it and try again.")
        return
    pull_ollama_model(model_name)

    research_topic = st.text_input("Enter your research topic:", research_topic_default)

    if st.button("Generate Solution"):
        with st.spinner("Generating solution..."):
            run_agents(research_topic)
        st.success("Generation complete! Please check the output above.")

# --- Click CLI ---

@click.command()
@click.option('--topic', prompt="Enter your research topic", default=research_topic_default)
def cli_app(topic):
    """Defines the Click CLI."""
    print("Skyscope Sentinel Multi-Agent AI Entrepreneur")
    print("Developed by: Casey J. Topojani")
    print("License: MIT")

    if not check_ollama_installed():
        print("Ollama is not installed. Please install it to continue.")
        sys.exit(1)
    pull_ollama_model(model_name)

    run_agents(topic)

# --- Run the App ---

if __name__ == '__main__':
    if "streamlit" in sys.argv[0]:
        streamlit_app()
    else:
        cli_app()
