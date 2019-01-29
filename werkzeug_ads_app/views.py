from werkzeug_ads_app.ads import AdsApp
from werkzeug_ads_app.models import Advertisement
from werkzeug.wrappers import Request, Response
from werkzeug.utils import redirect


class AdsAppWithViews(AdsApp):

    def display_advertisements(self, request: Request) -> Response:
        """
        Gets all advertisements from DB and render templates with its data.
        :param request: (Request obj)
        :return: (Response obj)
        """
        ads_list = self.database.get_sorted_collection_docs('advertisements', True)
        return self.render_template('home.html', data=ads_list)

    def add_advertisement(self, request: Request) -> Response:
        """
        Adds the new advertisement into DB and render main page template with its data.
        :param request: (Request obj)
        :return: (Response obj)
        """
        error = {}
        if request.method == 'POST':
            ad = Advertisement(request.form.get('title'), request.form.get('desc'))
            self.database.insert_document('advertisements', ad.generate_document())
            return redirect('/')
        return self.render_template('add_new.html', error=error)

    def get_admin_panel(self, request: Request) -> Response:
        """
        Remove all or the one advertisement from DB and render main page template with rest.
        :param request: (Request obj)
        :return: (Response obj)
        """

        ads_list = self.database.get_sorted_collection_docs('advertisements', True)
        if request.method == 'POST':
            if (request.form.get('del_all')):
                self.database.delete_all_docs_of_collection('advertisements')
            else:
                self.database.delete_one_doc_of_collection('advertisements', request.form.get('id'))
            return redirect('/admin')
        return self.render_template('admin.html', data=ads_list)
