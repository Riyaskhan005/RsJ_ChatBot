from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st

st.title("RsJ ChatBot")
input_txt = st.text_input("Enter your Quz")


prompt = ChatPromptTemplate.from_messages(
    [("system", "You are a helpful AI assistant. Your name is Rsj's assistant"),
     ("user", "user query:{query}")
    ]
)

llm = Ollama(model="llama2")
output_parser = StrOutputParser()
chain = prompt |llm|output_parser

if input_txt :
    st.write(chain.invoke({"query":input_txt}))