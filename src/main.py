import streamlit as st

from loguru import logger
from pathlib import Path

from langchain.llms import OpenAI, Ollama
# from langchain.prompts import PromptTemplate
# from langchain.chains import LLMChain
# from langchain.memory import ConversationBufferMemory
# from langchain.utilities import WikipediaAPIWrapper

# Directories and files
DIR_CURRENT = Path(__file__).parent
DIR_PROJECT = DIR_CURRENT.parent
DIR_LOGS = DIR_PROJECT / "logs"

# Check if logs directory exists
if not DIR_LOGS.exists():
    DIR_LOGS.mkdir()
    
# Setup Logging configuration
logger.add(
    DIR_LOGS / "main.log", 
    rotation="7 days", 
    level="DEBUG"
)

@logger.catch
def main() -> bool:
    
    # Define the following:
    # Model
    # LLMChain
    # Memory
    # Prompt Template
    # Streamlit App - Make it work first
    
    # Defining the model
    llm = Ollama(model="llama2:chat", temperature=0.9)
    
    st.set_page_config(
        layout='centered',
        initial_sidebar_state='collapsed'
    )
    
    # Insert header setup
    st.subheader("LLM-Chat using ollama")
    with st.expander("See for debugging purposes"):
        st.write(st.session_state)
        
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            
    # Accept user input
    if prompt := st.chat_input("Enter your prompt"):
        
        # Display user message in chat message container
        # Add user message to chat history
        with st.chat_message("user"):
            st.write(prompt)
        st.session_state.messages.append(
            {"role": "user", "content": prompt}
        )
        
        # Sample Response Only
        r = llm(prompt)
        
        # Display assistant r in chat message container
        # Add assistant r to chat history
        with st.chat_message("ai"):
            st.markdown(r)
            
        st.session_state.messages.append(
            {"role": "ai", "content": r}
        )
    
    return True


# Running the main function
if __name__ == "__main__":
    if main():
        logger.info("Running...")