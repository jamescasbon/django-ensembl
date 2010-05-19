from django.db import models
from ensembl.utils import reverse_complement


class StableIdManager(models.Manager):
    """ This manager will automatically follow some links """

    def get_query_set(self):
        return super(StableIdManager, self).get_query_set().select_related('stable_id')


class HasStableId(models.Model):
    """ Mixin that uses the stable id manager """
    
    class Meta:
        abstract = True
        
    objects = StableIdManager()
    
    def __unicode__(self):
        return self.stable_id.stable_id


class HasName(object):

    def __unicode__(self):
        return self.name
        

class HasSeqRegion(models.Model):

    # TODO: manager for this class

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
        
        # for c in components:
        #     print c.asm_start, c.asm_end, c.cmp_start, c.cmp_end, 
        # print coords
        
        # build the sequence from the component parts
        sequence = ''
        for (component,(start, end)) in zip(components, coords):
            # TODO: only fetch subseq 
            subseq = component.cmp_seq_region.dna.sequence[component.cmp_start-1:component.cmp_end]
            if component.ori== -1: subseq=reverse_complement(subseq)
            sequence += subseq[start:end]
            
        # reverse complement if necessary
        if self.seq_region_strand == -1: 
            sequence = reverse_complement(sequence)
        
        return sequence

