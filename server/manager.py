from server.models import Potager
from google.appengine.ext import ndb


class PotagersManager():

    @staticmethod
    def put(potager):
        potager.put()

    @staticmethod
    def list(start=0, pageSize=30):
        more = False
        ret = Potager.query().fetch(int(pageSize) + 1, offset=int(start))
        if len(ret) > int(pageSize):
            more = True
        return ret[0:int(pageSize)], more

    @staticmethod
    def get(id):
        return ndb.Key(Potager, int(id)).get()

    @staticmethod
    def delete(potager):
        return potager.key.delete()
