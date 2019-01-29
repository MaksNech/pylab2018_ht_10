import os
from werkzeug.wrappers import Request, Response
from werkzeug.exceptions import HTTPException, NotFound
from jinja2 import Environment, FileSystemLoader
from werkzeug_ads_app.database.mongo_db import MongoDB
from werkzeug_ads_app.config import MONGO_DB_CONFIG
from werkzeug_ads_app.urls import APP_URLS


class AdsApp(object):

    def __init__(self):
        """
        Constructor.
        :return (new Ads app obj)
        """
        self.database = MongoDB(MONGO_DB_CONFIG)
        template_path = os.path.join(os.path.dirname(__file__), 'templates/ads')
        self.jinja_env = Environment(loader=FileSystemLoader(template_path), autoescape=True)
        self.url_map = APP_URLS['ads_urls']


    def render_template(self, template_name: str, **context: dict) -> Response:
        """
        Renders template.
        :param template_name: (str)
        :param context: (dict)
        :return: (Response obj)
        """
        t = self.jinja_env.get_template(template_name)
        return Response(t.render(context), mimetype='text/html')

    def error_404(self)->Response:
        """
        Renders 404 error page.
        :return: (Response obj)
        """
        response = self.render_template('404.html')
        response.status_code = 404
        return response

    def dispatch_request(self, request: Request):
        """
        Binds the URL map to the current environment and get back a URLAdapter.
        The match method returns the endpoint and a dictionary of values in the URL.
        :param request: (Request)
        :return: (response as data)
        """
        adapter = self.url_map.bind_to_environ(request.environ)
        try:
            endpoint, values = adapter.match()
            return getattr(self, endpoint)(request, **values)
        except NotFound as e:
            return self.error_404()
        except HTTPException as e:
            return e

    def wsgi_app(self, environ, start_response)->Response:
        """
        :param environ: (The WSGI environment that the request object uses for data retrival.)
        :param start_response:
        :return: (response as a wsgi app)
        """
        request = Request(environ)
        response = self.dispatch_request(request)
        return response(environ, start_response)

    def __call__(self, environ, start_response):
        """
        :param environ: (The WSGI environment that the request object uses for data retrival.)
        :param start_response:
        :return: (wsgi app)
        """
        return self.wsgi_app(environ, start_response)
