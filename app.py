from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    name = "David Diaz"
    age = 25
    hobbies = ["coding", "reading", "gaming", "traveling"]
    return render_template("index.html", name=name, age=age, hobbies=hobbies)

if __name__ == "__main__":
    app.run(debug=True)