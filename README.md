# LocalGPT
<a name="readme-top"></a>
At this project I am creating my own chat llm applications that can be run on you local machine. The project is built on open source large language models manage by Ollama, and python library streamlit. LocalGPT is an open-source project that enables users to interact large language models (LLMs) locally, without an internet connection. 

![Reference](/.images/Sample.gif)

Here are some advantages and benefits of using LocalGPT.
- Privacy and Security: Since LocalGPT runs entirely on your own machine, it eliminates concerns about privacy and security associated with sending data to remote servers for processing. This is particularly important for sensitive data or applications where data privacy is a priority.
- Cost-Efficiency: Utilizing LocalGPT eliminates the need to pay for cloud-based services for model inference, which can be cost-effective, especially for applications with high usage or long-term needs.
- Low Latency: Running GPT locally can reduce latency because there's no need to send data over the internet to a remote server and wait for a response. This can be crucial for applications requiring real-time or near-real-time responses.
- Self-hosted: LocalGPT enables you to run your own AI model on your local machine, ensuring complete control over your data and privacy.
- Customizable: You can fine-tune the model to your specific needs, such as domain-specific knowledge or personal preferences.
- Open-source: LocalGPT is an open-source project, meaning you can contribute to its development and improve it for the community.
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started
### Prerequisite

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

### Running the Application

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

The roadmap is a guide for the author and contributors for the progression of the sample project, if decided to continue.
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
