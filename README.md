# LocalGPT
<a name="readme-top"></a>
Building your own chat llm applications.

### Benefits
- LocalGPT can be used to build your own chat applications.

## Getting Started
### Prerequisites

Before running the python streamlit application, you should have the following installed in your local machine. Currently, the application is working in WindowsOS machine, and not test in MacOS and LinuxOS.
1. Install the Python 3.9 or higher version, until 3.11.
2. Install the poetry library. The library will handle all your python dependencies and virtual environment in your local machine.
    ``` bash
    pip install poetry
    ```
3. Download and install ollama in your host machine. [Ollama](https://ollama.com/)
4. Pull the model by ollama command. The project is currently using llama2:chat model.
    ``` bash
    ollama pull --model=llama2:chat
    ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Installation

Ensure all prerequisites are met. You can run the application by *running the run.bat file* or by running the following command.
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

The roadmap is a guide for the author for the progression of this sample project. It may not be the most up-to-date.
- [ ] Sample Feature
    - [ ] Sample Nested Feature
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Acknowledgement 
Huge thanks to the following open source projects for inspiration and direction. The open sourced projects and/or videos have been great guidance to developing the project and personal growth.
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## References

These are other references and documentations used to develop the project.
- [OpenAI](https://openai.com)
- [Langchain](https://langchain.com)
- [Streamlit](https://streamlit.io)
- [Ollama](https://github.com/m-mizutani/ollama)
<p align="right">(<a href="#readme-top">back to top</a>)</p>