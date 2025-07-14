from flask import Flask, request, render_template, jsonify
from dotenv import load_dotenv
from rag_chain import setup_rag_chain

import os

app = Flask(__name__)
load_dotenv()

qa_chain = setup_rag_chain()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    try:
        user_prompt = request.form["prompt"]
        response = qa_chain({"query": user_prompt})
        answer = response["result"]
        sources = [
            {
                "page": doc.metadata.get("page", "N/A"),
                "content": doc.page_content
            }
            for doc in response.get("source_documents", [])
        ]
        return jsonify({"answer": answer, "sources": sources})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
