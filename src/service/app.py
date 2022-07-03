import falcon
from service.api.healthcheck import HealthCheckResource
from service.api.shortcode import ShorCodeResource
from service.api.shortcode import ShortCodeCreateResource
from service.api.shortcode import ShortCodeStatsResource


app = application = falcon.App()

app.add_route('/api/healthcheck', HealthCheckResource())
app.add_route('/api/url', ShortCodeCreateResource())
app.add_route('/api/url/{short_code}', ShorCodeResource())
app.add_route('/api/url/{short_code}/stats', ShortCodeStatsResource())
