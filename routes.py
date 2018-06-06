from views import handler, vs_heandler


def setup_routes(app):
    app.router.add_get('/', handler)
    app.router.add_get('/msg', vs_heandler)