from flask import Flask
from flask import request

from model import Urls
from model import db
from urlconverter import UrlConverter
from cache import Cache

app = Flask(__name__)
cache = Cache()

@app.route('/', methods=['GET'])
def index():
    return 'go /g/url geneate short url'

@app.route('/g', methods=['POST'])
def generate_short_url():
    origin_url = str(request.form['origin_url'])
    if not origin_url:
        # throw
        pass
    short_url = cache.get(origin_url)
    if short_url:
        return short_url
    id = Urls.query.filter_by(origin_url=origin_url).first()
    if not id:
        new_url = Urls(origin_url)
        db.session.add(new_url)
        db.session.commit()
        id = new_url.id
    short_url = UrlConverter.id_to_base62_url(id)
    # cache short_url
    cache.put(origin_url, short_url)
    return short_url

@app.route('/v/<short_url>', methods=['GET'])
def get_origin_url(short_url):
    origin_url = cache.get(short_url)
    if origin_url:
        return origin_url
    id = UrlConverter.base62_url_to_id(str(short_url))
    # get origin url from db by id
    origin_url = Urls.query.get_or_404(id).origin_url
    cache.put(short_url, origin_url)
    return origin_url

if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)
