import os
from dotenv import load_dotenv
from langchain_cohere import ChatCohere
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

load_dotenv()
llm = ChatCohere(model="command-xlarge-nightly", cohere_api_key="-")
memory = ConversationBufferMemory()
chatbot_chain = ConversationChain(llm=llm, memory=memory)
