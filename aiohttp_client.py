import aiohttp
import asyncio

import datetime

BASE_URL = 'http://0.0.0.0:8080'


a = f'{BASE_URL}/1/'
b = f'{BASE_URL}/2/'

start = datetime.datetime.now()

async def get(url, print_=False):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if print_:
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
tasks1001 = [asyncio.ensure_future(get(a)) for _ in range(500)] + [asyncio.ensure_future(get(a, print_=True))]

loop.run_until_complete(asyncio.wait(tasks1001))

print(datetime.datetime.now() - start)
