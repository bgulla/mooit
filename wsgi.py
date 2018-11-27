import os
import logging
from logging.handlers import RotatingFileHandler
from OpenSSL import SSL
from mooit import app

if __name__ == "__main__":
#    handler = RotatingFileHandler('access.log', maxBytes=10000, backupCount=1)
#    handler.setLevel(logging.INFO)
#    app.logger.addHandler(handler)
    context = SSL.Context(SSL.SSLv23_METHOD)
    cert_file = '/secret/cert/python-tls.crt'
    key_file = '/secret/cert/python-tls.key'
    if not os.path.exists('/secret/cert'):
        cert_file = './python-tls.crt'
        key_file = './python-tls.key'
    app.run(host="0.0.0.0",port=8443,ssl_context=(cert_file,key_file), debug=True)

