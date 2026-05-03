import pandas as pd
import pickle
import faiss
from sentence_transformers import SentenceTransformer

# Load dataset
df = pd.read_csv("data/qna.csv")

questions = df['question'].tolist()
answers = df['answer'].tolist()

# Load MiniLM model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Convert questions into embeddings
embeddings = model.encode(questions)

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# Save files
faiss.write_index(index, "model/faiss.index")

with open("model/answers.pkl", "wb") as f:
    pickle.dump(answers, f)

with open("model/questions.pkl", "wb") as f:
    pickle.dump(questions, f)

print("✅ Preprocessing done!")