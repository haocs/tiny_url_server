from flask import Flask
from flask import request

from model import Urls
from model import db
from urlconverter import UrlConverter

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return 'go /g/url geneate short url'

@app.route('/g', methods=['POST'])
def generate_short_url():
    origin_url = str(request.form['origin_url'])
    new_url = Urls(origin_url)
    db.session.add(new_url)
    db.session.commit()
    id = new_url.id
    shrot_url = UrlConverter.id_to_base62_url(id)
    return shrot_url

@app.route('/v/<short_url>', methods=['GET'])
def get_origin_url(short_url):
    id = UrlConverter.base62_url_to_id(str(short_url))
    # get origin url from db by id
    url = Urls.query.get_or_404(id)
    return url.origin_url

if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)
