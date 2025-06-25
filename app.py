from flask import Flask, render_template, request, jsonify, session
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import OllamaLLM

app = Flask(__name__)
app.secret_key = "your_secret_key"
llm = OllamaLLM(model="mistral")
llm.invoke("Hello") 
output_parser = StrOutputParser()

@app.route("/")
def index():
    session["history"] = []
    return render_template("chat.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json.get("message", "")
    history = session.get("history", [])
    history.append(("user", user_input))

    # Build prompt messages correctly for ChatPromptTemplate
    messages = [("system", "You are a helpful AI assistant. Your name is RsJ's assistant")]
    # Append history in (role, content) format
    messages.extend(history)

    prompt = ChatPromptTemplate.from_messages(messages)

    # Build chain once outside if possible (optional)
    chain = prompt | llm | output_parser

    response = chain.invoke({})

    history.append(("assistant", response))
    session["history"] = history 
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)