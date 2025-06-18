from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
    return 'Exfil Server is Live'

@app.route('/exfil', methods=['POST'])
def exfil():
    data = request.get_data(as_text=True)
    with open("exfil.txt", "a") as f:
        f.write(data + "\n")
    return '', 204

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
