class EnsemblRouter(object):
    """ Base class for routing, allows reads and prevents everything else"""

    app = None
    database = None

    def db_for_read(self, model, **hints):
        if model._meta.app_label == self.app:
            return self.database
        return None

    def db_for_write(self, model, **hints):
        return None

    def allow_relation(self, obj1, obj2, **hints):
        return None

    def allow_syncdb(self, db, model):
        return None


class CoreRouter(EnsemblRouter):
    app = 'core'
    database = 'ensembl.core'