from flask import Flask, render_template, redirect, url_for, request, session, flash, g, abort
from functools import wraps
import logging
import cowsay
from logging.handlers import RotatingFileHandler
import datetime


application = Flask(__name__)


@application.route('/', methods=['GET', 'POST']) #this is called a decorator
def home():
    cow = cowsay.cowsay("moo")
    if request.method == 'POST':
        if request.form['text']:
            moo_text = request.form['text']
            cow = cowsay.cowsay(moo_text)
#            application.logger.info('[Moo] '+ unicode(now.replace(microsecond=0)) + "\t" + request.remote_addr + "\t" + moo_text)
    return render_template("index.html", cow=cow)

# API
@application.route('/api/cow', methods=['GET', 'POST'])
def api():
    if request.method == 'POST':
        if request.form['text']:
            return cowsay.cowsay(request.form['text'])
    else:

        abort(400, 'missing POST[test] field')
    return

# Custom 404 page
@application.errorhandler(404)
def page_not_found(e):
#    application.logger.error('[ERROR] ' + request.remote_addr + "\t404\t" + request.url)
    return render_template('404.html'), 404

# Start the server with the 'run()' method
if __name__ == '__main__':
    handler = RotatingFileHandler('/tmp/mooit.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    application.logger.addHandler(handler)
    application.run(host="0.0.0.0",debug=True)
