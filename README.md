# LocalGPT
Building your own chat llm applications.

## Getting Started

### Prerequisites

Before running the python application, you should have the following installed in your local machine. The application runs properly in WindowsOS machine.
1. Install the python 3.9 or higher version, until 3.11.
2. Install the poetry library. This python library will handle all your python dependencies and virtual environment in your local machine.
    ``` bash
    pip install poetry
    ```
3. Download and install ollama in your host machine. [Ollama](https://ollama.com/)
4. Pull the model using ollama command. Here we are using llama2:chat model.
``` bash
ollama pull --model=llama2:chat
```

### Installation

You can run the following application using the following command:

```bash
poetry install

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