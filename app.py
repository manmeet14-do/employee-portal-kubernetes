from flask import Flask, render_template, jsonify

app = Flask(__name__)

employees = [
    {"id": 1, "name": "Manmeet Kaur", "department": "DevOps"},
    {"id": 2, "name": "John Doe", "department": "Development"},
    {"id": 3, "name": "Jane Smith", "department": "Testing"}
]

@app.route('/')
def home():
    return render_template('index.html', employees=employees)

@app.route('/health')
def health():
    return jsonify({"status": "UP"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
