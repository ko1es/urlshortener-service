
from pydantic import BaseModel


class DataBase(BaseModel):
    database: str
    user: str
    password: str
    host: str
    # port: int = 5432
    scheme: str = 'mongodb'

    def get_connection_url(self) -> str:
        return f'{self.scheme}://{self.user}:{self.password}@{self.host}'


class ServiceConfig(BaseModel):
    service_name: str = 'getmatch-urlshortener-service'


class Config(BaseModel):
    database: DataBase
    service: ServiceConfig


class HealthCheckStatus(BaseModel):
    db: bool
