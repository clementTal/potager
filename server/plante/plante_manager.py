from server.plante.plante_models import Plante
from google.appengine.ext import ndb

def put(potager):
    potager.put()

def list(start=0, pageSize=30):
    more = False
    ret = Plante.query().fetch(int(pageSize) + 1, offset=int(start))
    if len(ret) > int(pageSize):
        more = True
    return ret[0:int(pageSize)], more

def get(id):
    return ndb.Key(Plante, int(id)).get()

def delete(potager):
    return potager.key.delete()