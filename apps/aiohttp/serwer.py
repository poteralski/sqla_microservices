from aiohttp import web

from apps.aiohttp.extensions import db


class Handler1(web.View):
    async def get(self):
        s = (db.session())
        response = web.Response(text=f"{id(s)}")
        return response


class Handler2(web.View):
    async def get(self):
        s = (db.session())
        response = web.Response(text=f"{id(s)}")
        return response


class App(web.Application):
    _current_request = 0
    config = {}

    def get_current_request(self):
        return self._current_request
