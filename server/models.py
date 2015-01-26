from google.appengine.ext import ndb


class Potager(ndb.Model):
    name = ndb.StringProperty()
    info = ndb.JsonProperty()