import unittest
from django.db import models


class BasicTest(object):

    model = None

    def test_lookup_object(self):
        assert self.model.objects.all()[0]


class StableIdTest(object):

    def test_stable_id(self):
        assert self.model.objects.all()[0].stable_id


class SeqRegionTest(object):

    def test_seq_region(self):
        assert self.model.objects.all()[0].seq_region


