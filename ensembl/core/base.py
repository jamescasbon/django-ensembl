from django.db import models


class StableIdManager(models.Manager):
    """ This manager will automatically join on the stable id table"""

    def get_query_set(self):
        return super(StableIdManager, self).get_query_set().select_related('stable_id')


class HasStableId(models.Model):
    """ Mixin that uses the stable id manager """
    
    class Meta:
        abstract = True
        
    objects = StableIdManager()

    @property
    def stable_id(self):
        return self._stable_id.stable_id
    
    def __unicode__(self):
        return self.stable_id


class HasName(object):

    def __unicode__(self):
        return self.name
        

class HasSeqRegion(models.Model):

    class Meta:
        abstract = True

    seq_region = models.ForeignKey('SeqRegion')
    seq_region_start = models.IntegerField()
    seq_region_end = models.IntegerField()
