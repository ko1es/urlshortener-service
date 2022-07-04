
import falcon
from service.exceptions import ShortCodeNotFound
from service.models import Source
from service.repository import SourceRepository
from service.types import ShortCode


class BaseResource:

    def __init__(self) -> None:
        self.repository = SourceRepository()


class ShortCodeCreateResource(BaseResource):

    # TODO: add schema vlidator with @before decorator
    def on_post(self, request, response) -> None:
        # POST запрос на <hostname>/urls с оригинальной ссылкой, генерирует новый короткий URL, и возвращает его в формате <hostname>/urls/<short code>, где <short code> это короткий уникальный "код" ссылки
        data = request.media
        source_id: SourceId = self.repository.insert(
            Source(origin=data['origin']),
        )
        try:
            source = self.repository.get_by_id(source_id)
        except ShortCodeNotFound as e:
            response.media = {'res': source_id}
        else:
            response.media = {'result': f'url/{source.short_code}'}
            response.status = falcon.HTTP_201


class ShorCodeResource(BaseResource):

    def on_get(self, request, response, short_code: ShortCode) -> None:
        # GET запрос на <hostname>/urls/<short code> перенаправляет пользователя на оригинальную ссылку
        try:
            source: Source = self.repository.get_by_code(short_code=short_code)
        except ShortCodeNotFound as e:
            response.media = {'error': e.message}
            response.status = falcon.HTTP_404
        except InvalidParamException as e:
            response.message = {'error': e.message}
            response.status = falcon.HTTP_400
        else:
            self.repository.update_touch_count(
                short_code=source.short_code,
                touch_count=source.touch_count + 1,
            )
            raise falcon.HTTPMovedPermanently(source.origin)

    # TODO: add schema vlidator with @before decorator
    def on_put(self, request, response, short_code: ShortCode) -> None:
        # PUT запрос на <hostname>/urls/<short code> с новой ссылкой обновляет существующую короткую ссылку
        self.repository.update_url(
            short_code=short_code, url=request.media['origin'],
        )
        response.status = falcon.HTTP_200
        response.media = {'result': 'updated'}

    def on_delete(self, request, response, short_code: ShortCode) -> None:
        # DELETE запрос на <hostname>/urls/<short code> удаляет короткую ссылку
        self.repository.delete_by_short_code(short_code=short_code)
        response.status = falcon.HTTP_204


class ShortCodeStatsResource(BaseResource):

    def on_get(self, request, response, short_code: ShortCode) -> None:
        # GET запрос на <hostname>/urls/<short code>/stats возвращает количество переходов по ссылке за последние 24 часа
        try:
            source: Source = self.repository.get_by_code(short_code=short_code)
        except ShortCodeNotFound as e:
            response.media = {'result': e.message}
            response.status = falcon.HTTP_404
        except InvalidParamException as e:
            response.message = {'error': e.message}
            response.status = falcon.HTTP_400
        else:
            response.media = {'redirects': source.touch_count}
            response.status = falcon.HTTP_200
