import falcon
import json 
import secrets
from service.types import ShortCode
from service.storage import SourceStorage
from service.models import Source

class BaseResource:

    def __init__(self) -> None:
        self.storage = SourceStorage()


class ShortCodeCreateResource(BaseResource):
        
    def on_post(self, request, response) -> None:
        # POST запрос на <hostname>/urls с оригинальной ссылкой, генерирует новый короткий URL, и возвращает его в формате <hostname>/urls/<short code>, где <short code> это короткий уникальный "код" ссылки
        data = request.media
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        short_code = "".join(secrets.choice(chars) for _ in range(5))
        result: ShortCode = self.storage.insert(
            Source(short_code = short_code, origin=data['origin']),
        )
        # response.media = {'result': data['url']}
        response.media = {'result': f'url/{result}'}
        response.status = falcon.HTTP_201
    

class ShorCodeResource(BaseResource):

    def on_put(self, request, response, short_code: ShortCode) -> None:
        # PUT запрос на <hostname>/urls/<short code> с новой ссылкой обновляет существующую короткую ссылку
        response.status = falcon.HTTP_200
        response.media = {'test': short_code}

    def on_get(self, request, response, short_code: ShortCode) -> None:
        # GET запрос на <hostname>/urls/<short code> перенаправляет пользователя на оригинальную ссылку
        response.text = json.dumps({'result rrr': short_code}, ensure_ascii=False)
        response.status = falcon.HTTP_200

    def on_delete(self, request, response, short_code: ShortCode) -> None:
        # DELETE запрос на <hostname>/urls/<short code> удаляет короткую ссылку
        response.text = json.dumps({'result': short_code})
        response.status = falcon.HTTP_204


class ShortCodeStatsResource:

    def on_get(self, request, response, short_code: ShortCode) -> None:
        # GET запрос на <hostname>/urls/<short code>/stats возвращает количество переходов по ссылке за последние 24 часа
        response.text = json.dumps({'result': short_code})
        response.status = falcon.HTTP_200
