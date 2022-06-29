import os

from settings.models import Config
from settings.models import DataBase
from settings.models import ServiceConfig
from settings.models import RabbitMQ


CONFIG = Config(
    database=DataBase(
        database=os.environ['POSTGRES_DB'],
        user=os.environ['POSTGRES_USER'],
        password=os.environ['POSTGRES_PASSWORD'],
    ),
    service=ServiceConfig(),
        rabbitmq=RabbitMQ(
        user=os.environ['RABBITMQ_USER'],
        password=os.environ['RABBITMQ_PASSWORD'],
    )
)
