import falcon
from .api import ShortURLResource

short_url = ShortURLResource()

app = application = falcon.App()
app.add_route('/api/url', short_url)
