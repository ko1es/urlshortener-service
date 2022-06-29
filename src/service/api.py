import falcon


class ShortURLResource:

    def on_get(self, request, response) -> None:
        resp.text = json.dumps({'result': 'ok'}, ensure_ascii=False)

        resp.status = falcon.HTTP_200
