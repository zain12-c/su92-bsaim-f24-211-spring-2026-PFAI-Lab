from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def get_reply(user_input):
    msg = user_input.lower()

    # Using a mapping is more "Senior Dev" style than a bunch of IFs
    responses = {
        "emergency": "Call 1122 immediately or head to the emergency ward.",
        "doctor": "We have specialists in Cardiology, Neurology, and General Surgery.",
        "appointment": "Appointments can be booked online via our portal or at the reception desk.",
        "visiting": "Standard visiting hours are 4 PM to 8 PM daily.",
        "department": "Main Departments: Emergency, Pediatrics, Orthopedics, and Cardiology.",
        "pharmacy": "Our in-house pharmacy is open 24/7.",
        "hi": "Hello! I'm the Hospital Assistant. How can I help?",
        "hello": "Hello! I'm the Hospital Assistant. How can I help?"
    }

    # Check for keywords in the message
    for key, response in responses.items():
        if key in msg:
            return response

    return "I'm not sure about that. Try asking about appointments, departments, or pharmacy hours."

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def handle_chat():
    # Grabbing data using .get() is safer and more common in real-world apps
    user_text = request.form.get("message", "")
    bot_response = get_reply(user_text)
    
    return jsonify({"reply": bot_response})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)