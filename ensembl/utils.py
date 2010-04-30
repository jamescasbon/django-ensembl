import unittest
import string


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
        
    def test_sequence_lookup_returns_object_of_correct_length(self):
        example = self.model.objects.all()[0]
        assert len(example.sequence) == example.seq_region_end - example.seq_region_start

    # def test_sequence_lookup_returns_object_in_correct_orientation(self):
    #     assert(False)


_rc_trans = string.maketrans('ACGTN', 'TGCAN')
def reverse_complement(seq):
    return string.translate(str(seq), _rc_trans)[::-1]
