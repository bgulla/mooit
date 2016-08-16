from flask import Flask, render_template, redirect, url_for, request, session, flash, g
from functools import wraps
import cowsay

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST']) #this is called a decorator
def home():
    cow = cowsay.cowsay("moo")
    if request.method == 'POST':
        if request.form['text']:
            cow = cowsay.cowsay(request.form['text'])
    return render_template("index.html", cow=cow)


# Start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)