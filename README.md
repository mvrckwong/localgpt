# LocalGPT
Building your own chat llm applications.

### Benefits
- LocalGPT can be used to build your own chat applications.

## Overview
- [LocalGPT](#localgpt)
    - [Benefits](#benefits)
  - [Overview](#overview)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Roadmap](#roadmap)
  - [Acknowledgement](#acknowledgement)
    - [Other References](#other-references)
  - [Contact](#contact)
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started

### Prerequisites

Before running the python streamlit application, you should have the following installed in your local machine. Currently, the application is working in WindowsOS machine, and not test in MacOS and LinuxOS.
1. Install the Python 3.9 or higher version, until 3.11.
2. Install the poetry library. The library will handle all your python dependencies and virtual environment in your local machine.
    ``` bash
    pip install poetry
    ```
3. Download and install ollama in your host machine. [Ollama](https://ollama.com/)
4. Pull the model using ollama command. Here we are using llama2:chat model.
    ``` bash
    ollama pull --model=llama2:chat
    ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Installation

You can run the application using by *running the run.bat file* or by running the following command.
- Run the command to install the virtual environment and all the dependencies.
    ```bash
    poetry install
    ```
- Run the streamlit application
    ```bash
    poetry run streamlit run src/main.py
    ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Roadmap

## Acknowledgement 
Huge thanks to the following open source projects for inspiration and direction.

### Other References
- [OpenAI](https://openai.com)
- [Langchain](https://langchain.com)
- [Streamlit](https://streamlit.io)
- [Ollama](https://github.com/m-mizutani/ollama)
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contact
- [GitHub](https://github.com/mvrckwong)
- [Linkedin](https://www.linkedin.com/in/mvrckwong/)
- [Hashnode](https://hashnode.com/@mvrckwong)
<p align="right">(<a href="#readme-top">back to top</a>)</p>