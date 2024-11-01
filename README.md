Skyscope Sentinel Multi-Agent AI Entrepreneur Researcher and Autonomous Agent
==============================================================================

**Developed By:** Casey J. Topojani** License:** MIT

Overview
--------

The **Skyscope Sentinel Multi-Agent AI Entrepreneur** is a powerful application designed to help users research, develop, and implement a six-figure automated passive income solution focused on cryptocurrency, all from the comfort of home. Leveraging the strengths of open-source language models and the collaborative features of CrewAI, this application provides an actionable roadmap to achieve crypto income goals.

Features
--------

*   **Research and Development**: AI-driven agents research existing crypto income strategies, analyze opportunities, and generate concrete steps for implementation.
    
*   **Actionable Plan**: Produces a detailed, beginner-friendly plan with specific resources, tools, and instructions.
    
*   **Beginner-Friendly**: Designed for users with minimal technical experience, offering clear, accessible instructions.
    
*   **WebUI and CLI**: Access the tool via an interactive web interface (Streamlit) or through a command-line interface (Click).
    
*   **Progress Tracking**: Real-time progress tracking with a live progress bar and verbose output to monitor the AI's actions and task progression.
    

Installation
------------

### **Step 1: Install Dependencies**

Ensure you have the required Python packages installed:

pip install streamlit click langchain crewai crewai-tools duckduckgo-search ollama tqdm

### **Step 2: Download the Code**

Clone the repository by running 'git clone https://github.com/skyscope-sentinel/Skyscope-Sentinel-AI-Entrepreneur.git'
Enter the directory cloned 'cd Skyscope-Sentinel-AI-Entrepreneur'

### **Step 3: Set up LLM/s**
Ensure you have installed ollama already
Download locally the required ollama model 'ollama pull internlm2.5:latest'

Usage
-----

### Streamlit Web UI

1.  Launch the Streamlit app:
    

streamlit run SkyscopeSentinelEntrepreneur.py

1.  Enter your research topic in the input field.
    
2.  Click "Generate Solution" to initiate the research process.
    
3.  View the generated research report and implementation plan in the results section.
    

### Command-Line Interface (CLI)

1.  Run the CLI version:
    

python SkyscopeSentinelEntrepreneur.py

Enter your research topic when prompted

The AI will generate and display the research report and implementation plan in the console

Contributing
------------

Contributions are welcome! Please open an issue or submit a pull request with suggestions or improvements.

Disclaimer
----------

**Skyscope Sentinel Intelligence** provides this open-source application as a community resource for educational and informational purposes only. Users are responsible for ensuring their actions comply with all local laws and regulations. This application is not intended to offer financial, legal, or professional advice. Always do your own research and consult qualified professionals before making any investment or business decisions.

Skyscope Sentinel Intelligence disclaims responsibility for any misuse, malicious use, or illegal activities involving this code. Users are solely responsible for ensuring ethical use of this application.

Note on Model Configuration
---------------------------

This application uses an Ollama model (internml2.5). Adjust the model\_name variable in the code if using a different Ollama model.

To ensure the python application will work without error please ensure you have ollama installed and lastly ensure you have performed ‘ollama pull internml2.5:latest’
