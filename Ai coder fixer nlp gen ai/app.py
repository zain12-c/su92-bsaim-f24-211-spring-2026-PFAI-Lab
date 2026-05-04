import os
from flask import Flask, render_template, request, jsonify
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(
    api_key="AIzaSyDNdn12Om21lQ8e5kLesdMgINgfYTsF8cU", 
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/fix', methods=['POST'])
def fix_code():
    data = request.get_json()
    user_code = data.get("code")

    if not user_code:
        return jsonify({"result": "Error: Please provide some code."}), 400

    try:
   
        response = client.chat.completions.create(
            model="gemini-3-flash-preview", 
            messages=[
                {
                    "role": "system", 
                    "content": "You are a senior AI coding assistant. Return the fixed code first in a markdown block, then a simple list of what was wrong."
                },
                {
                    "role": "user", 
                    "content": f"Fix this code and explain the errors:\n\n{user_code}"
                }
            ],
            temperature=0.1
        )

        result = response.choices[0].message.content
        return jsonify({"result": result})

    except Exception as e:

        print(f"Debug Log: {str(e)}")
        return jsonify({"result": f"API Error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)