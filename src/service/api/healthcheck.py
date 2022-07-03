from falcon import Request, Response

from settings.models import HealthCheckStatus
from settings.db import check_connection


class HealthCheckResource:

    def on_get(self, request: Request, response: Response):
        response.media = HealthCheckStatus(db=check_connection()).dict()
