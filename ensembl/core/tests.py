"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""
from unittest import TestCase

from ensembl.utils import BasicTest, StableIdTest, SeqRegionTest
from models import *


class ExonTest(TestCase, StableIdTest, SeqRegionTest):
    
    model = Exon
        
    def test_transcripts(self):
        assert Exon.objects.all()[0].transcripts.all()
        
        
class TranscriptTest(TestCase, StableIdTest, SeqRegionTest):

    model = Transcript

    def test_exons(self):
        transcript = Transcript.objects.all()[0]
        assert transcript.exons.all()
        
    def test_gene(self):
        Transcript.objects.all()[0].gene
        

class GeneTest(TestCase, StableIdTest, SeqRegionTest):
    
    model = Gene
    
    def test_transcripts(self):
        assert Gene.objects.all()[0].transcript_set.all()
        
    def test_canonical_transcript(self):
        assert Gene.objects.all()[0].canonical_transcript
    
    
class SeqRegionTest(TestCase, BasicTest):
    
    model = SeqRegion
    
    def test_coord_system(self):
        assert SeqRegion.objects.all()[0].coord_system
        
    def test_exons(self):
        assert SeqRegion.objects.all()[0].exon_set
    
    def test_transcripts(self):
        assert SeqRegion.objects.all()[0].transcript_set
    
    

