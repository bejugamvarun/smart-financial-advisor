# src/rag/langchain_integration.py
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

llm = OpenAI(api_key='your_gpt_4_api_key')


def create_retrieval_chain(retriever):
    prompt_template = PromptTemplate(
        input_variables=["context", "query"],
        template="Context: {context}\nQuery: {query}\nAnswer:"
    )

    qa_chain = RetrievalQA(
        retriever=retriever,
        llm=llm,
        prompt_template=prompt_template
    )
    return qa_chain
