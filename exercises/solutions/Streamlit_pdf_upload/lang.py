import os
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.schema.output_parser import StrOutputParser
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema.runnable import RunnablePassthrough
from langchain.prompts import PromptTemplate
from langchain.vectorstores.utils import filter_complex_metadata

def initialize_model():
    """Initialize the OpenAI chat model."""
    return ChatOpenAI(model="gpt-4", temperature=0)

def initialize_prompt():
    """Create and return a prompt template."""
    return PromptTemplate.from_template(
        """
        <s> [INST] You are an assistant for question-answering tasks. Use the following pieces of retrieved context 
        to answer the question. If you don't know the answer, just say that you don't know. Use three sentences
        maximum and keep the answer concise. [/INST] </s> 
        [INST] Question: {question} 
        Context: {context} 
        Answer: [/INST]
        """
    )

def ingest_pdf(pdf_file_path: str):
    """Ingest a PDF, process it into chunks, and create a retriever."""
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1024, chunk_overlap=100)
    docs = PyPDFLoader(file_path=pdf_file_path).load()
    chunks = text_splitter.split_documents(docs)
    chunks = filter_complex_metadata(chunks)

    vector_store = Chroma.from_documents(documents=chunks, embedding=OpenAIEmbeddings())
    retriever = vector_store.as_retriever(
        search_type="similarity_score_threshold",
        search_kwargs={
            "k": 3,
            "score_threshold": 0.5,
        },
    )
    return retriever

def build_chain(retriever, model, prompt):
    """Build the question-answering chain."""
    return ({"context": retriever, "question": RunnablePassthrough()}
            | prompt
            | model
            | StrOutputParser())

def ask_question(chain, query: str):
    """Ask a question using the chain."""
    if not chain:
        return "Please, add a PDF document first."

    return chain.invoke(query)

def clear_chain():
    """Clear all components for resetting the system."""
    return None, None, None