from werkzeug.routing import Map, Rule

"""
APP_URLS contain all urls of the app. 
"""
APP_URLS = {
    'ads_urls': Map([
        Rule('/', endpoint='display_advertisements'),
        Rule('/add', endpoint='add_advertisement'),
        Rule('/admin', endpoint='get_admin_panel')
    ]),
}
