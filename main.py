import os
from werkzeug.wsgi import SharedDataMiddleware
from werkzeug_ads_app.views import AdsAppWithViews
from werkzeug_ads_app.config import APP_CONFIG
from werkzeug.serving import run_simple


def create_ads_app(with_static=True):
    """
    Creates ads app.
    :param with_static: (bool)
    :return: (AdsAppWithViews obj)
    """
    app = AdsAppWithViews()
    if with_static:
        app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
            '/static': os.path.join(os.path.dirname(__file__), 'werkzeug_ads_app/static')
        })
    return app


if __name__ == '__main__':
    app = create_ads_app()
    run_simple(APP_CONFIG['host'], APP_CONFIG['port'], app, use_debugger=True, use_reloader=True)
