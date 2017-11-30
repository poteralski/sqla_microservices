import aiohttp
import asyncio

import datetime

BASE_URL = 'http://0.0.0.0:8080'


a = f'{BASE_URL}/1/'
b = f'{BASE_URL}/2/'


async def get(url):
    print('GET: ', url)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            t = '{0:%H:%M:%S}'.format(datetime.datetime.now())
            print('Done: {}, {} ({})'.format(t, response.url, response.status))
            print(await response.read())

loop = asyncio.get_event_loop()
tasks = [
    asyncio.ensure_future(get(a)),
    asyncio.ensure_future(get(a)),
    asyncio.ensure_future(get(a)),
    asyncio.ensure_future(get(b)),
    asyncio.ensure_future(get(b)),
    asyncio.ensure_future(get(b))
]
loop.run_until_complete(asyncio.wait(tasks))