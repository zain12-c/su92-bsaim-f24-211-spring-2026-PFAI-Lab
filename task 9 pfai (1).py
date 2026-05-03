from collections import Counter

# Input data
raw_text = """Natural Language Processing is a field of Artificial Intelligence.
It helps computers understand human language.
It is used in chatbots, translation, and sentiment analysis.
NLP is very useful in modern applications."""

# Standardize and tokenize
tokens = raw_text.lower().split()
freqs = Counter(tokens)

# Split by sentences (simple split is more common for quick scripts)
lines = [s.strip() for s in raw_text.split('.') if s.strip()]

scores = {}

for s in lines:
    # A dev would likely use a list comprehension or a generator here
    words = s.lower().split()
    scores[s] = sum(freqs.get(w, 0) for w in words)

# Get the top line
best_sentence = max(scores, key=scores.get)

print(f"--- Original ---\n{raw_text}")
print(f"\n--- Summary ---\n{best_sentence}")