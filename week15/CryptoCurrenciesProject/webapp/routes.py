import json

from flask import render_template
from requests import Session

from webapp import app

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '15daef1e-3fcc-46e5-8dcb-694f950ab633',
}

session = Session()
session.headers.update(headers)


@app.route('/', methods=['GET'])
def index():
    response = session.get('https://pro-api.coinmarketcap.com/v1/cryptocurrency/map')
    data = json.loads(response.text)['data']
    return render_template('index.html', data=data)
