import os
from dotenv import load_dotenv
from langchain_cohere import ChatCohere
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

load_dotenv()
llm = ChatCohere(model="command-xlarge-nightly", cohere_api_key="-")
template = "You are an academic writer. Generate a {type} on: {topic}"
prompt = PromptTemplate(input_variables=["type", "topic"], template=template)
generator_chain = LLMChain(llm=llm, prompt=prompt)
