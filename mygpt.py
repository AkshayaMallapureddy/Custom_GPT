#imports

from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
#code

#prompt

prompt1 = ChatPromptTemplate.from_messages([
   ("system","Listen to whatever user says"),
   ("user","give a precise answer to the question{question}") 
])

#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
#llama-3.3-70b-versatile


#LLM

llm = ChatGroq(
    model = "gemma2-9b-it",
    groq_api_key="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",
    temperature = 0
)

#output

op = StrOutputParser()


#chain
chain = prompt1 | llm | op

#streamlit
st.title("CUSTOM GPT")
input_text = st.text_input("enter the question")
output = chain.invoke({"question":input_text})
st.write(output)