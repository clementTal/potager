import webapp2
import json
from server import jsonEncode
from server.plante import plante_manager
from server.plante.plante_models import Plante

class PlanteService(webapp2.RequestHandler):

    def get(self):
        key = self.request.url.split('/')[-1]
        response = {}
        ## get a list of plants
        if key == 'list':
            plantes, more = plante_manager.list()
            response = {
                'plantes': plantes,
                'more': more
            }
        ## get on plant with given key
        else:
            plante = plante_manager.get(key)
            response = {
                'plante': plante,
            }

        self.response.write(jsonEncode.encode(response))

    def post(self):
        key = self.request.url.split('/')[-1]
        response = {
            'message': 'Ajout potager'
        }
        if key == 'add':
            planteMessage = json.loads(self.request.body)
            plante = Plante()
            plante.name = planteMessage.get('nom', '')
            plante.famille = planteMessage.get('FamillePlante', '')
            plante.soleil = planteMessage.get('SoleilPlante', '')
            plante.type = planteMessage.get('TypePlante', '')
            plante.cycleCulture = planteMessage.get('cycleCulture', '')
            plante.hauteur = planteMessage.get('hauteurPlante', 0)
            plante.nbCarre = planteMessage.get('nbCarreRequis', 0)
            plante.qteCarre = planteMessage.get('quantiteCarre', 0)
            plante.recole = planteMessage.get('recolte:', [])
            plante.semis = planteMessage.get('semisTerre', [])
            plante.protection = planteMessage.get('semisTerreProtection', [])
            plante.sol = planteMessage.get('sol', '')
            plante.tpsOccupation =  planteMessage.get('tempsOccupationCarre', 0)
            plante.tpsRotation = planteMessage.get('tempsRotationCarre', 0)
            plante.variete = planteMessage.get(' variete', '')
            plante_manager.put(plante)

        self.response.write(jsonEncode.encode(response))

    def put(self):
        pass

    def delete(self):
        id = self.request.url.split('/')[-1]
        response = {
            'message': 'Supression de la plante'
        }
        plante = plante_manager.get(id)
        plante_manager.delete(plante)
        self.response.write(jsonEncode.encode(response))