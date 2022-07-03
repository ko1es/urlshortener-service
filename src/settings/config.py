import os

from settings.models import Config
from settings.models import DataBase
from settings.models import ServiceConfig


CONFIG = Config(
    database=DataBase(
        scheme=os.environ['DB_SCHEME'],
        database=os.environ['DB_NAME'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD'],
        host=os.environ['DB_HOST']
    ),
    service=ServiceConfig(),
)
