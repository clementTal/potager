from google.appengine.ext import ndb


class Plante(ndb.Model):
    name = ndb.StringProperty(required=True)
    soleil = ndb.StringProperty()
    variete = ndb.StringProperty()
    famille = ndb.StringProperty()
    type = ndb.StringProperty()
    cycleCulture = ndb.StringProperty()
    hauteur = ndb.IntegerProperty()
    nbCarre = ndb.IntegerProperty()
    qteCarre = ndb.IntegerProperty()
    recole = ndb.IntegerProperty(repeated=True)
    semis = ndb.IntegerProperty(repeated=True)
    protection = ndb.IntegerProperty(repeated=True)
    sol = ndb.StringProperty()
    tpsOccupation = ndb.IntegerProperty()
    tpsRotation = ndb.IntegerProperty()

