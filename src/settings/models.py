from pydantic import BaseModel
from typing import Optional


class DataBase(BaseModel):
    database: str
    user: str
    password: str
    host: str = 'database'
    port: int = 5432
    driver: str = 'postgresql'

    def get_connection_url(self) -> str:
        return f'{self.driver}://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}'


class ServiceConfig(BaseModel):
    service_name: str = '<name>-service'


class RabbitMQ(BaseModel):
    user: str
    password: str
    port: int = 5672
    host: str = 'rabbitmq'

    def get_connection_url(self) -> str:
        # return "amqp://guest:guest@rabbitmq:5672/"
        return f"amqp://{self.user}:{self.password}@{self.host}:{self.port}/"


class Config(BaseModel):
    database: DataBase
    service: ServiceConfig
    rabbitmq: Optional[RabbitMQ] = None
