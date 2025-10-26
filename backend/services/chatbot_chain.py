import os
from dotenv import load_dotenv
from langchain_cohere import ChatCohere
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

load_dotenv()
llm = ChatCohere(model="command-xlarge-nightly", cohere_api_key="W9T9D3DGjtqAEgPEAJlr0J8GWYMLDwSNm4EqYi3Y")
memory = ConversationBufferMemory()
chatbot_chain = ConversationChain(llm=llm, memory=memory)
