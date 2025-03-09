from flask import Flask, request, jsonify

app = Flask(__name__)

# Chatbot function
def simple_chatbot(user_query):
    responses = {
        "What is the total revenue?": "The total revenue is $10 million.",
        "How has net income changed over the last year?": "The net income has increased by $2 million over the last year.",
        "What is the profit margin?": "The profit margin is 15%."
    }
    
    return responses.get(user_query, "Sorry, I can only provide information on predefined queries.")

# Flask Web App
@app.route("/chatbot", methods=["GET"])
def chatbot():
    user_query = request.args.get("query")
    if not user_query:
        return jsonify({"error": "Please provide a query"}), 400
    response = simple_chatbot(user_query)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
