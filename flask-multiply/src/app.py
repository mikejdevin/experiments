from flask import Flask, render_template
import random

app = Flask(__name__)

# list names
rnames = ["bob","cody","jim"]

@app.route('/')
def index():
    url = random.choice(rnames)
    return render_template('index.html', name=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
