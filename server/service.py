import webapp2
from server import jsonEncode
from server.manager import PotagersManager
from server.models import Potager

class Service(webapp2.RequestHandler):

    def get(self):

        potager, more = PotagersManager.list()
        response = {
            'potager': potager,
            'more': more
        }
        self.response.write(jsonEncode.encode(response))

    def post(self):
        pass

    def put(self):
        response = {
            'message': 'Ajout potager'
        }
        potager = Potager()
        potager.name = 'toto'
        potager.info = jsonEncode.encode({'param1': 'patates', 'param2': 'radis', 'param3': 'courgettes'})
        PotagersManager.put(potager)

        self.response.write(jsonEncode.encode(response))

    def delete(self):
        id = self.request.url.split('/')[-1]
        response = {
            'message': 'Supression potager'
        }
        potager = PotagersManager.get(id)
        PotagersManager.delete(potager)
        self.response.write(jsonEncode.encode(response))