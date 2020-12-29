from flask import Flask, render_template
import numpy as np
import random

app = Flask(__name__)

# list names
rnames = ["alice","bob"]

@app.route('/')
def index():
    url = random.choice(rnames)
    return render_template('index.html', name=url)

@app.route('/byte/')
def byte_api():

    return { "test": np.zeros(12) }

if __name__ == "__main__":
    app.run(host="127.0.0.1")
