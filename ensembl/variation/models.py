from django.db import models

from ensembl.core.models import HasSeqRegion, HasName, HasStableId


# class Allele(models.Model):
#     allele_id = models.IntegerField(primary_key=True)
#     variation_id = models.IntegerField()
#     subsnp_id = models.IntegerField(null=True, blank=True)
#     allele = models.CharField(max_length=765, blank=True)
#     frequency = models.FloatField(null=True, blank=True)
#     sample_id = models.IntegerField(null=True, blank=True)
#     class Meta:
#         db_table = u'allele'
# 
# class AlleleGroup(models.Model):
#     allele_group_id = models.IntegerField(primary_key=True)
#     variation_group_id = models.IntegerField()
#     sample_id = models.IntegerField(null=True, blank=True)
#     name = models.CharField(unique=True, max_length=765, blank=True)
#     source_id = models.IntegerField(null=True, blank=True)
#     frequency = models.FloatField(null=True, blank=True)
#     class Meta:
#         db_table = u'allele_group'
# 
# class AlleleGroupAllele(models.Model):
#     allele_group_id = models.IntegerField()
#     allele = models.CharField(max_length=765)
#     variation_id = models.IntegerField()
#     class Meta:
#         db_table = u'allele_group_allele'
# 
# class CompressedGenotypeSingleBp(models.Model):
#     sample_id = models.IntegerField()
#     seq_region_id = models.IntegerField()
#     seq_region_start = models.IntegerField()
#     seq_region_end = models.IntegerField()
#     seq_region_strand = models.IntegerField()
#     genotypes = models.TextField(blank=True)
#     class Meta:
#         db_table = u'compressed_genotype_single_bp'
# 
# class FailedDescription(models.Model):
#     failed_description_id = models.IntegerField(primary_key=True)
#     description = models.TextField()
#     class Meta:
#         db_table = u'failed_description'
# 
# class FailedVariation(models.Model):
#     variation_id = models.IntegerField(primary_key=True)
#     failed_description_id = models.IntegerField()
#     class Meta:
#         db_table = u'failed_variation'
# 
# class FlankingSequence(models.Model):
#     variation_id = models.IntegerField(primary_key=True)
#     up_seq = models.TextField(blank=True)
#     down_seq = models.TextField(blank=True)
#     up_seq_region_start = models.IntegerField(null=True, blank=True)
#     up_seq_region_end = models.IntegerField(null=True, blank=True)
#     down_seq_region_start = models.IntegerField(null=True, blank=True)
#     down_seq_region_end = models.IntegerField(null=True, blank=True)
#     seq_region_id = models.IntegerField(null=True, blank=True)
#     seq_region_strand = models.IntegerField(null=True, blank=True)
#     class Meta:
#         db_table = u'flanking_sequence'
# 
# class Httag(models.Model):
#     httag_id = models.IntegerField(primary_key=True)
#     variation_group_id = models.IntegerField()
#     name = models.CharField(max_length=765, blank=True)
#     source_id = models.IntegerField()
#     class Meta:
#         db_table = u'httag'
# 
# class Individual(models.Model):
#     sample_id = models.IntegerField(primary_key=True)
#     gender = models.CharField(max_length=21)
#     father_individual_sample_id = models.IntegerField(null=True, blank=True)
#     mother_individual_sample_id = models.IntegerField(null=True, blank=True)
#     individual_type_id = models.IntegerField()
#     class Meta:
#         db_table = u'individual'
# 
# class IndividualGenotypeMultipleBp(models.Model):
#     variation_id = models.IntegerField()
#     subsnp_id = models.IntegerField(null=True, blank=True)
#     allele_1 = models.CharField(max_length=765, blank=True)
#     allele_2 = models.CharField(max_length=765, blank=True)
#     sample_id = models.IntegerField(null=True, blank=True)
#     class Meta:
#         db_table = u'individual_genotype_multiple_bp'
# 
# class IndividualPopulation(models.Model):
#     individual_sample_id = models.IntegerField()
#     population_sample_id = models.IntegerField()
#     class Meta:
#         db_table = u'individual_population'
# 
# class IndividualType(models.Model):
#     individual_type_id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=765)
#     description = models.TextField(blank=True)
#     class Meta:
#         db_table = u'individual_type'
# 
# class Meta(models.Model):
#     meta_id = models.IntegerField(primary_key=True)
#     species_id = models.IntegerField(null=True, blank=True)
#     meta_key = models.CharField(unique=True, max_length=120)
#     meta_value = models.CharField(max_length=765)
#     class Meta:
#         db_table = u'meta'
# 
# class MetaCoord(models.Model):
#     table_name = models.CharField(unique=True, max_length=120)
#     coord_system_id = models.IntegerField(unique=True)
#     max_length = models.IntegerField(null=True, blank=True)
#     class Meta:
#         db_table = u'meta_coord'
# 
# class Phenotype(models.Model):
#     phenotype_id = models.IntegerField(primary_key=True)
#     name = models.CharField(unique=True, max_length=150, blank=True)
#     description = models.CharField(max_length=765, blank=True)
#     class Meta:
#         db_table = u'phenotype'
# 
# class Population(models.Model):
#     sample_id = models.IntegerField(primary_key=True)
#     class Meta:
#         db_table = u'population'
# 
# class PopulationGenotype(models.Model):
#     population_genotype_id = models.IntegerField(primary_key=True)
#     variation_id = models.IntegerField()
#     subsnp_id = models.IntegerField(null=True, blank=True)
#     allele_1 = models.CharField(max_length=765, blank=True)
#     allele_2 = models.CharField(max_length=765, blank=True)
#     frequency = models.FloatField(null=True, blank=True)
#     sample_id = models.IntegerField(null=True, blank=True)
#     class Meta:
#         db_table = u'population_genotype'
# 
# class PopulationStructure(models.Model):
#     super_population_sample_id = models.IntegerField()
#     sub_population_sample_id = models.IntegerField()
#     class Meta:
#         db_table = u'population_structure'
# 
# class ReadCoverage(models.Model):
#     seq_region_id = models.IntegerField()
#     seq_region_start = models.IntegerField()
#     seq_region_end = models.IntegerField()
#     level = models.IntegerField()
#     sample_id = models.IntegerField()
#     class Meta:
#         db_table = u'read_coverage'
# 
# class Sample(models.Model):
#     sample_id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=765)
#     size = models.IntegerField(null=True, blank=True)
#     description = models.TextField(blank=True)
#     display = models.CharField(max_length=39, blank=True)
#     class Meta:
#         db_table = u'sample'
# 
# class SampleSynonym(models.Model):
#     sample_synonym_id = models.IntegerField(primary_key=True)
#     sample_id = models.IntegerField()
#     source_id = models.IntegerField()
#     name = models.CharField(max_length=765, blank=True)
#     class Meta:
#         db_table = u'sample_synonym'
# 
# class SeqRegion(models.Model):
#     seq_region_id = models.IntegerField(primary_key=True)
#     name = models.CharField(unique=True, max_length=120)
#     class Meta:
#         db_table = u'seq_region'
 
class Source(models.Model):
    source_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765, blank=True)
    version = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'source'

# class SubsnpHandle(models.Model):
#     subsnp_id = models.IntegerField(primary_key=True)
#     handle = models.CharField(max_length=60, blank=True)
#     class Meta:
#         db_table = u'subsnp_handle'
# 
# class TaggedVariationFeature(models.Model):
#     variation_feature_id = models.IntegerField(primary_key=True)
#     sample_id = models.IntegerField(primary_key=True)
#     class Meta:
#         db_table = u'tagged_variation_feature'
# 
# class TranscriptVariation(models.Model):
#     transcript_variation_id = models.IntegerField(primary_key=True)
#     transcript_id = models.IntegerField()
#     variation_feature_id = models.IntegerField()
#     cdna_start = models.IntegerField(null=True, blank=True)
#     cdna_end = models.IntegerField(null=True, blank=True)
#     translation_start = models.IntegerField(null=True, blank=True)
#     translation_end = models.IntegerField(null=True, blank=True)
#     peptide_allele_string = models.CharField(max_length=765, blank=True)
#     consequence_type = models.CharField(max_length=717)
#     class Meta:
#         db_table = u'transcript_variation'
 
class Variation(models.Model, HasName):
    variation_id = models.IntegerField(primary_key=True)
    source = models.ForeignKey('Source')
    name = models.CharField(unique=True, max_length=765, blank=True)
    validation_status = models.CharField(max_length=138, blank=True)
    ancestral_allele = models.TextField(blank=True)
    class Meta:
        db_table = u'variation'
 
# class VariationAnnotation(models.Model):
#     variation_annotation_id = models.IntegerField(primary_key=True)
#     variation_id = models.IntegerField()
#     phenotype_id = models.IntegerField()
#     source_id = models.IntegerField()
#     study = models.CharField(max_length=90, blank=True)
#     study_type = models.CharField(max_length=12, blank=True)
#     local_stable_id = models.CharField(max_length=765, blank=True)
#     associated_gene = models.CharField(max_length=765, blank=True)
#     associated_variant_risk_allele = models.CharField(max_length=765, blank=True)
#     variation_names = models.CharField(max_length=765, blank=True)
#     risk_allele_freq_in_controls = models.CharField(max_length=90, blank=True)
#     p_value = models.CharField(max_length=60, blank=True)
#     class Meta:
#         db_table = u'variation_annotation'
 
class VariationFeature(HasSeqRegion):
    variation_feature_id = models.IntegerField(primary_key=True)
    # seq_region_id = models.IntegerField()
    # seq_region_start = models.IntegerField()
    # seq_region_end = models.IntegerField()
    seq_region_strand = models.IntegerField()
    variation = models.ForeignKey('Variation')
    allele_string = models.TextField(blank=True)
    variation_name = models.CharField(max_length=765, blank=True)
    map_weight = models.IntegerField()
    flags = models.CharField(max_length=27, blank=True)
    source_id = models.IntegerField()
    validation_status = models.CharField(max_length=117, blank=True)
    consequence_type = models.CharField(max_length=795)
    class Meta:
        db_table = u'variation_feature'
 
# class VariationGroup(models.Model):
#     variation_group_id = models.IntegerField(primary_key=True)
#     name = models.CharField(unique=True, max_length=765, blank=True)
#     source_id = models.IntegerField()
#     type = models.CharField(max_length=27, blank=True)
#     class Meta:
#         db_table = u'variation_group'
# 
# class VariationGroupFeature(models.Model):
#     variation_group_feature_id = models.IntegerField(primary_key=True)
#     seq_region_id = models.IntegerField()
#     seq_region_start = models.IntegerField()
#     seq_region_end = models.IntegerField()
#     seq_region_strand = models.IntegerField()
#     variation_group_id = models.IntegerField()
#     variation_group_name = models.CharField(max_length=765, blank=True)
#     class Meta:
#         db_table = u'variation_group_feature'
# 
# class VariationGroupVariation(models.Model):
#     variation_id = models.IntegerField()
#     variation_group_id = models.IntegerField()
#     class Meta:
#         db_table = u'variation_group_variation'
# 
# class VariationSynonym(models.Model):
#     variation_synonym_id = models.IntegerField(primary_key=True)
#     variation_id = models.IntegerField()
#     subsnp_id = models.IntegerField(null=True, blank=True)
#     source_id = models.IntegerField()
#     name = models.CharField(unique=True, max_length=765, blank=True)
#     moltype = models.CharField(max_length=150, blank=True)
#     class Meta:
#         db_table = u'variation_synonym'
# 
