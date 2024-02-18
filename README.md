# LocalGPT
Building your own chat llm applications.

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

### Installation

You can run the application using by *running the run.bat file* or by running the following command.
- Run the command to install the virtual environment and all the dependencies.
    ```bash
    poetry install
    ```

    ```bash
    poetry run streamlit run src/main.py
    ```


## Contact
- [GitHub](https://github.com/mvrckwong)
- [Linkedin](https://www.linkedin.com/in/mvrckwong/)
- [Hashnode](https://hashnode.com/@mvrckwong)

## Acknowledgement 
- [OpenAI](https://openai.com)
- [Langchain](https://langchain.com)
- [Streamlit](https://streamlit.io)
- [Ollama](https://github.com/m-mizutani/ollama)