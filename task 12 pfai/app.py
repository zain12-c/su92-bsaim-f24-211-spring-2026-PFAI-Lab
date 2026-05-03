from flask import Flask, render_template, request, jsonify
import pickle
import faiss
from sentence_transformers import SentenceTransformer

app = Flask(__name__)

# Load model + data
model = SentenceTransformer('all-MiniLM-L6-v2')
index = faiss.read_index("model/faiss.index")

with open("model/answers.pkl", "rb") as f:
    answers = pickle.load(f)

# Search function
def get_reply(user_input):
    query_vector = model.encode([user_input])
    
    D, I = index.search(query_vector, k=1)
    
    return answers[I[0][0]]

@app.route("/")
def index_page():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_text = request.form.get("message")
    reply = get_reply(user_text)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)  