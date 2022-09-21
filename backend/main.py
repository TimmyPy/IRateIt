from aiohttp import web

from apps.category.views import Category

if __name__ == '__main__':
    app = web.Application()
    app.add_routes([
        web.view('/api/v1/category', Category)  # Use web.route to build routes
                                                # by config
    ])
    web.run_app(app)
