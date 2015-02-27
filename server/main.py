import logging
import os
import jinja2
import webapp2
from google.appengine.ext.webapp.util import run_wsgi_app
from server.plante.plante_service import PlanteService

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(os.path.dirname(__file__))),
    variable_start_string='[[',
    variable_end_string=']]'
)


class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('./pages/index.html')
        self.response.out.write(template.render({}))

application = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/api/plante.*', PlanteService)
], debug=True)


def main():
    logging.getLogger().setLevel(logging.DEBUG)
    run_wsgi_app(application)

if __name__ == '__main__':
    main()
