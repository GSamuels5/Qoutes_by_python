from flask import Flask, render_template
import requests

app = Flask(__name__)
app.debug = True  # Enable debugging mode

@app.route("/")
def index():
    url = "https://api.quotable.io/random"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        quote = data["content"]
        author = data["author"]
        return render_template("./index.html", quote=quote, author=author)
    else:
        return f"Error: {response.status_code}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)