from aiohttp.web import middleware

from apps.aiohttp.extensions import db


@middleware
async def sqla_middleware(request, handler):
    request.app._current_request = id(request)
    resp = await handler(request)
    db.session.remove()
    return resp
