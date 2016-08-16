from flask import Flask, render_template, redirect, url_for, request, session, flash, g, abort
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

# API
@app.route('/api/cow', methods=['GET', 'POST'])
def api():
    if request.method == 'POST':
        if request.form['text']:
            return cowsay.cowsay(request.form['text'])
    else:
        abort(400, 'missing POST[test] field')
    return

# Custom 404 page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Start the server with the 'run()' method
if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)