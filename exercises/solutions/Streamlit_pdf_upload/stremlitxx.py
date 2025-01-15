import streamlit as st
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.schema.output_parser import StrOutputParser
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain.vectorstores.utils import filter_complex_metadata

# Functions for backend logic
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

def ingest_pdf(pdf_file_path):
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
    return ({'context': retriever, 'question': RunnablePassthrough()}
            | prompt
            | model
            | StrOutputParser())

# Streamlit frontend
st.title("📄 Ask the Doc App")
st.markdown("Upload et pdf dokument, stil dit spørgsmål og få et svar fra openAI.") 

# File uploader
uploaded_file = st.file_uploader("Upload en PDF fil", type=["pdf"])

# Input fields
question = st.text_input("Stil dit spørgsmål:", placeholder="Giv mig et kort resume ef denne tekst")
api_key = st.text_input("OpenAI API Key", type="password")

# Submit button
if st.button("Submit"):
    if uploaded_file and question and api_key:
        # Save the uploaded file temporarily
        with open("temp.pdf", "wb") as f:
            f.write(uploaded_file.read())

        try:
            # Initialize backend components
            st.info("Processing document...")
            model = ChatOpenAI(model="gpt-4", temperature=0, openai_api_key=api_key)
            prompt = initialize_prompt()
            retriever = ingest_pdf("temp.pdf")
            chain = build_chain(retriever, model, prompt)

            # Get the answer
            st.info("Venter på svar...")
            response = chain.invoke(question)
            st.success(f"Answer: {response}")

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    else:
        st.error("Please upload a PDF, enter your question, and provide your OpenAI API key.")

