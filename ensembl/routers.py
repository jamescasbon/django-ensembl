class EnsemblRouter(object):
    """ Base class for routing, allows reads and prevents everything else"""

    # TODO: fix the app_labels to be ensembl.core rather than core
    db_lookup = {
        'core': 'ensembl.core',
        'variation': 'ensembl.variation'
    }    

    def db_for_read(self, model, **hints):
        return self.db_lookup.get(model._meta.app_label, 'default')

    def allow_syncdb(self, db, model):
        if model._meta.app_label in self.db_lookup: 
            return False
