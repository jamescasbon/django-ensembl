"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""
from unittest import TestCase
from ensembl.utils import BasicTest, StableIdTest, SeqRegionTest
from models import *


class VariationTest(TestCase, BasicTest):
    
    model = Variation
    
    def test_variation_features(self):
        assert Variation.objects.all()[0].variationfeature_set.all()


class VariationFeatureTest(TestCase, SeqRegionTest):
    
    model = VariationFeature
        
    def test_variation(self):
        assert VariationFeature.objects.all()[0].variation        
        