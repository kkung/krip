import os
from flask import Flask, json, make_response, request
from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug.contrib.fixers import ProxyFix

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db = SQLAlchemy(app)
app.wsgi_app = ProxyFix(app.wsgi_app)

from .models import KRIPAddress, KRIPAddressEncoder

@app.route('/', defaults={'address': None})
@app.route('/<address>')
def lookup(address):
    if address is None:
        address = request.args.get('address', request.remote_addr)

    def _lookup():
        try:
            addr = KRIPAddress.find_by_ipaddr(address)
            if not addr:
                raise ValueError('%s was not assigned by KRNIC' % address)
            else:
                return (True, addr)
        except ValueError as e:
            return (False, str(e))

    result, addr = _lookup()

    jsonp = request.args.get('callback', None)
    resp_content = json.dumps({
        'result': result,
        'return_value': addr
    }, cls=KRIPAddressEncoder)

    if jsonp:
        resp_content = '%s(%s)' % (str(jsonp), resp_content)

    response = make_response(resp_content)
    response.mimetype = 'application/json'
    return response
