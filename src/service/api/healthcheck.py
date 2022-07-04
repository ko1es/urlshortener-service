from falcon import Request
from falcon import Response
from settings.db import check_connection
from settings.models import HealthCheckStatus


class HealthCheckResource:

    def on_get(self, request: Request, response: Response):
        response.media = HealthCheckStatus(db=check_connection()).dict()
