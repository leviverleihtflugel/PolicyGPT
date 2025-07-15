from flask import Flask, render_template, request
from rag_engine import query

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    answer = {"steps": ""}
    if request.method == "POST":
        question = request.form["question"]
        result = query(question)
        answer["steps"] = result.get("steps", "")
    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run(debug=True)
