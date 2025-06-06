from flask import Flask, render_template, request, jsonify
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

app = Flask(__name__)

# Initialize LangChain objects
llm = Ollama(model="llama2")
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant. Your name is Rsj's assistant"),
    ("user", "user query:{query}")
])
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json.get("message", "")
    response = chain.invoke({"query": user_input})
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)