from aiohttp import web

from apps.aiohttp.extensions import db
from apps.aiohttp.models import Example


class Handler1(web.View):
    async def get(self):
        s = (db.session())
        s.add(Example())
        s.commit()
        count = len(s.query(Example).all())
        response = web.Response(text=f"{id(s)} elements in db {count}")
        return response


class Handler2(web.View):
    async def get(self):
        s = (db.session())
        response = web.Response(text=f"{id(s)}")
        return response


class App(web.Application):
    _current_request = None
    config = {}

    def get_current_request(self):
        return self._current_request
