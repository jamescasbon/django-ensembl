from django.db import models
from ensembl.utils import reverse_complement


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
    seq_region_strand = models.IntegerField()
    
    def sequence_level_assemblies(self):
        """return the set of assemblies at the sequence level for this object"""
        return self.seq_region.assembly_asm_set.filter(
            cmp_seq_region__coord_system__attrib__contains='sequence_level'
            ).filter(
                asm_start__lt=self.seq_region_start
            ).filter(
                asm_end__gt=self.seq_region_end
            )
            
    def projected_coords(self, assemblies):
        """ project the coordinates of this object into assemblies """
        return [
            (
                max(self.seq_region_start - component.asm_start,0) + component.cmp_start, 
                min(self.seq_region_end - component.asm_start + component.cmp_start, component.cmp_end)
            )
            for component in assemblies
        ]

    @property 
    def sequence(self):
        """return the sequence for this object"""
        
        # fetch the component assemblies and their DNA and project coords into those
        components = self.sequence_level_assemblies().select_related('cmp_seq_region__dna').all()
        coords = self.projected_coords(components)
        
        # build the sequence from the component parts
        sequence = ''.join([
            component.cmp_seq_region.dna.sequence[start:end]
            for (component,(start, end)) in zip(components, coords)
        ])
        
        # reverse complement if necessary
        if self.seq_region_strand == -1: 
            sequence = reverse_complement(sequence)
        
        return sequence

