import os
from dotenv import load_dotenv
from langchain_cohere import CohereEmbeddings, ChatCohere
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader
from langchain.chains import ConversationalRetrievalChain

load_dotenv()
cohere_api_key = os.getenv("COHERE_API_KEY")
embeddings = CohereEmbeddings(model="embed-english-light-v3.0", cohere_api_key="W9T9D3DGjtqAEgPEAJlr0J8GWYMLDwSNm4EqYi3Y")
llm = ChatCohere(model="command-xlarge-nightly", cohere_api_key="W9T9D3DGjtqAEgPEAJlr0J8GWYMLDwSNm4EqYi3Y")
vectorstore = None
memory = []

def store_document(file_path):
    global vectorstore
    loader = PyPDFLoader(file_path)
    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = splitter.split_documents(docs)
    vectorstore = FAISS.from_documents(chunks, embeddings)

def query_document(query):
    global vectorstore
    if not vectorstore:
        return "No document uploaded."
    chain = ConversationalRetrievalChain.from_llm(llm, vectorstore.as_retriever())
    result = chain.invoke({"question": query, "chat_history": []})
    return result["answer"]
