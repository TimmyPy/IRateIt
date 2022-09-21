from aiohttp import web


class Category(web.View):
    async def get(self):
        return web.Response(text='Hello world')
