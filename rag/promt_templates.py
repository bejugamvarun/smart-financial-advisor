# src/rag/prompt_templates.py
from langchain.prompts import PromptTemplate


def get_prompt_template():
    return PromptTemplate(
        input_variables=["context", "query"],
        template="Context: {context}\n\nQuery: {query}\n\nAnswer:"
    )
