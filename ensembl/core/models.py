from django.db import models

from base import HasStableId, HasName, HasStableId, HasSeqRegion


# class AltAllele(models.Model):
#     alt_allele_id = models.IntegerField(unique=True)
#     gene_id = models.IntegerField(unique=True)
#     class Meta:
#         db_table = u'alt_allele'
# 
# class Analysis(models.Model):
#     analysis_id = models.IntegerField(primary_key=True)
#     created = models.DateTimeField()
#     logic_name = models.CharField(unique=True, max_length=255)
#     db = models.CharField(max_length=360, blank=True)
#     db_version = models.CharField(max_length=120, blank=True)
#     db_file = models.CharField(max_length=360, blank=True)
#     program = models.CharField(max_length=240, blank=True)
#     program_version = models.CharField(max_length=120, blank=True)
#     program_file = models.CharField(max_length=240, blank=True)
#     parameters = models.TextField(blank=True)
#     module = models.CharField(max_length=240, blank=True)
#     module_version = models.CharField(max_length=120, blank=True)
#     gff_source = models.CharField(max_length=120, blank=True)
#     gff_feature = models.CharField(max_length=120, blank=True)
#     class Meta:
#         db_table = u'analysis'
# 
# class AnalysisDescription(models.Model):
#     analysis_id = models.IntegerField(unique=True)
#     description = models.TextField(blank=True)
#     display_label = models.CharField(max_length=765)
#     displayable = models.IntegerField()
#     web_data = models.TextField(blank=True)
#     class Meta:
#         db_table = u'analysis_description'


class Assembly(models.Model):
    asm_seq_region = models.ForeignKey('SeqRegion', related_name='assembly_asm_set', primary_key=True)
    cmp_seq_region = models.ForeignKey('SeqRegion', related_name='assembly_cmp_set', primary_key=True)
    asm_start = models.IntegerField(primary_key=True)
    asm_end = models.IntegerField(unique=True, primary_key=True)
    cmp_start = models.IntegerField(unique=True, primary_key=True)
    cmp_end = models.IntegerField(unique=True, primary_key=True)
    ori = models.IntegerField(unique=True)
    
    class Meta:
        db_table = u'assembly'


# class AssemblyException(models.Model):
#     assembly_exception_id = models.IntegerField(primary_key=True)
#     seq_region_id = models.IntegerField()
#     seq_region_start = models.IntegerField()
#     seq_region_end = models.IntegerField()
#     exc_type = models.CharField(max_length=9)
#     exc_seq_region_id = models.IntegerField()
#     exc_seq_region_start = models.IntegerField()
#     exc_seq_region_end = models.IntegerField()
#     ori = models.IntegerField()
#     class Meta:
#         db_table = u'assembly_exception'
# 
# class AttribType(models.Model):
#     attrib_type_id = models.IntegerField(primary_key=True)
#     code = models.CharField(unique=True, max_length=45)
#     name = models.CharField(max_length=765)
#     description = models.TextField(blank=True)
#     class Meta:
#         db_table = u'attrib_type'


class CoordSystem(models.Model, HasName):
    coord_system_id = models.IntegerField(primary_key=True)
    species_id = models.IntegerField()
    name = models.CharField(unique=True, max_length=120)
    version = models.CharField(unique=True, max_length=255, blank=True)
    rank = models.IntegerField(unique=True)
    attrib = models.CharField(max_length=90, blank=True)
    class Meta:
        db_table = u'coord_system'


# class DensityFeature(models.Model):
#     density_feature_id = models.IntegerField(primary_key=True)
#     density_type_id = models.IntegerField()
#     seq_region_id = models.IntegerField()
#     seq_region_start = models.IntegerField()
#     seq_region_end = models.IntegerField()
#     density_value = models.FloatField()
#     class Meta:
#         db_table = u'density_feature'
# 
# class DensityType(models.Model):
#     density_type_id = models.IntegerField(primary_key=True)
#     analysis_id = models.IntegerField(unique=True)
#     block_size = models.IntegerField(unique=True)
#     region_features = models.IntegerField(unique=True)
#     value_type = models.CharField(max_length=15)
#     class Meta:
#         db_table = u'density_type'
# 
# class DependentXref(models.Model):
#     object_xref_id = models.IntegerField(primary_key=True)
#     master_xref_id = models.IntegerField()
#     dependent_xref_id = models.IntegerField()
#     class Meta:
#         db_table = u'dependent_xref'
# 
# class Ditag(models.Model):
#     ditag_id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=90)
#     type = models.CharField(max_length=90)
#     tag_count = models.IntegerField()
#     sequence = models.TextField()
#     class Meta:
#         db_table = u'ditag'
# 
# class DitagFeature(models.Model):
#     ditag_feature_id = models.IntegerField(primary_key=True)
#     ditag_id = models.IntegerField()
#     ditag_pair_id = models.IntegerField()
#     seq_region_id = models.IntegerField()
#     seq_region_start = models.IntegerField()
#     seq_region_end = models.IntegerField()
#     seq_region_strand = models.IntegerField()
#     analysis_id = models.IntegerField()
#     hit_start = models.IntegerField()
#     hit_end = models.IntegerField()
#     hit_strand = models.IntegerField()
#     cigar_line = models.TextField()
#     ditag_side = models.CharField(max_length=3)
#     class Meta:
#         db_table = u'ditag_feature'


class Dna(models.Model):
    seq_region = models.OneToOneField('SeqRegion', primary_key=True)
    sequence = models.TextField()
    class Meta:
        db_table = u'dna'

 
# class DnaAlignFeature(models.Model):
#     dna_align_feature_id = models.IntegerField(primary_key=True)
#     seq_region_id = models.IntegerField()
#     seq_region_start = models.IntegerField()
#     seq_region_end = models.IntegerField()
#     seq_region_strand = models.IntegerField()
#     hit_start = models.IntegerField()
#     hit_end = models.IntegerField()
#     hit_strand = models.IntegerField()
#     hit_name = models.CharField(max_length=120)
#     analysis_id = models.IntegerField()
#     score = models.FloatField(null=True, blank=True)
#     evalue = models.FloatField(null=True, blank=True)
#     perc_ident = models.FloatField(null=True, blank=True)
#     cigar_line = models.TextField(blank=True)
#     external_db_id = models.IntegerField(null=True, blank=True)
#     hcoverage = models.FloatField(null=True, blank=True)
#     external_data = models.TextField(blank=True)
#     pair_dna_align_feature_id = models.IntegerField(null=True, blank=True)
#     class Meta:
#         db_table = u'dna_align_feature'
# 
# class Dnac(models.Model):
#     seq_region_id = models.IntegerField(primary_key=True)
#     sequence = models.TextField()
#     n_line = models.TextField(blank=True)
#     class Meta:
#         db_table = u'dnac'


class Exon(HasSeqRegion, HasStableId):
    exon_id = models.IntegerField(primary_key=True)
    # seq_region_id = models.IntegerField()
    # seq_region_start = models.IntegerField()
    # seq_region_end = models.IntegerField()
    # seq_region_strand = models.IntegerField()
    phase = models.IntegerField()
    end_phase = models.IntegerField()
    is_current = models.IntegerField()
    is_constitutive = models.IntegerField()
    class Meta:
        db_table = u'exon'
        
    transcripts = models.ManyToManyField('Transcript', 
        related_name='exons', 
        db_table='exon_transcript'
    )


class ExonStableId(models.Model):
    exon = models.OneToOneField('Exon', primary_key=True, related_name='stable_id')
    stable_id = models.CharField(max_length=384)
    version = models.IntegerField(null=True, blank=True)
    created_date = models.DateTimeField()
    modified_date = models.DateTimeField()
    class Meta:
        db_table = u'exon_stable_id'


##### ExonTranscript is specified by the ManyToManyField Exon.transcripts
#   
class ExonTranscript(models.Model):
    exon = models.ForeignKey(Exon)
    transcript = models.ForeignKey('Transcript')
    rank = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'exon_transcript'

class ExternalDb(models.Model):
    external_db_id = models.IntegerField(primary_key=True)
    db_name = models.CharField(max_length=300)
    db_release = models.CharField(max_length=765, blank=True)
    status = models.CharField(max_length=27)
    dbprimary_acc_linkable = models.IntegerField()
    display_label_linkable = models.IntegerField()
    priority = models.IntegerField()
    db_display_name = models.CharField(max_length=765, blank=True)
    type = models.CharField(max_length=54, blank=True)
    secondary_db_name = models.CharField(max_length=765, blank=True)
    secondary_db_table = models.CharField(max_length=765, blank=True)
    description = models.TextField(blank=True)
    class Meta:
        db_table = u'external_db'
#
# class ExternalSynonym(models.Model):
#     xref_id = models.IntegerField(primary_key=True)
#     synonym = models.CharField(max_length=120)
#     class Meta:
#         db_table = u'external_synonym'


class Gene(HasSeqRegion, HasStableId):
    gene_id = models.IntegerField(primary_key=True)
    biotype = models.CharField(max_length=120)
    analysis_id = models.IntegerField()
    # seq_region_id = models.IntegerField()
    # seq_region_start = models.IntegerField()
    # seq_region_end = models.IntegerField()
    # seq_region_strand = models.IntegerField()
    display_xref = models.ForeignKey('Xref', null=True, blank=True)
    source = models.CharField(max_length=60)
    status = models.CharField(max_length=57, blank=True)
    description = models.TextField(blank=True)
    is_current = models.IntegerField()
    canonical_transcript = models.ForeignKey('Transcript', related_name='_gene')
    canonical_annotation = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'gene'


# class GeneArchive(models.Model):
#     gene_stable_id = models.CharField(max_length=384)
#     gene_version = models.IntegerField()
#     transcript_stable_id = models.CharField(max_length=384)
#     transcript_version = models.IntegerField()
#     translation_stable_id = models.CharField(max_length=384, blank=True)
#     translation_version = models.IntegerField(null=True, blank=True)
#     peptide_archive_id = models.IntegerField(null=True, blank=True)
#     mapping_session_id = models.IntegerField()
#     class Meta:
#         db_table = u'gene_archive'
# 
# class GeneAttrib(models.Model):
#     gene_id = models.IntegerField()
#     attrib_type_id = models.IntegerField()
#     value = models.TextField()
#     class Meta:
#         db_table = u'gene_attrib'


class GeneStableId(models.Model):
    gene = models.OneToOneField('Gene', primary_key=True, related_name='stable_id')
    stable_id = models.CharField(max_length=384)
    version = models.IntegerField(null=True, blank=True)
    created_date = models.DateTimeField()
    modified_date = models.DateTimeField()
    class Meta:
        db_table = u'gene_stable_id'


# class GoXref(models.Model):
#     object_xref_id = models.IntegerField(unique=True)
#     linkage_type = models.CharField(unique=True, max_length=9, blank=True)
#     source_xref_id = models.IntegerField(null=True, blank=True)
#     class Meta:
#         db_table = u'go_xref'
# 
# class IdentityXref(models.Model):
#     object_xref_id = models.IntegerField(primary_key=True)
#     xref_identity = models.IntegerField(null=True, blank=True)
#     ensembl_identity = models.IntegerField(null=True, blank=True)
#     xref_start = models.IntegerField(null=True, blank=True)
#     xref_end = models.IntegerField(null=True, blank=True)
#     ensembl_start = models.IntegerField(null=True, blank=True)
#     ensembl_end = models.IntegerField(null=True, blank=True)
#     cigar_line = models.TextField(blank=True)
#     score = models.FloatField(null=True, blank=True)
#     evalue = models.FloatField(null=True, blank=True)
#     class Meta:
#         db_table = u'identity_xref'
# 
# # class Interpro(models.Model):
# #     interpro_ac = models.CharField(unique=True, max_length=120)
# #     id = models.CharField(max_length=120)
# #     class Meta:
# #         db_table = u'interpro'
# 
# class Karyotype(models.Model):
#     karyotype_id = models.IntegerField(primary_key=True)
#     seq_region_id = models.IntegerField()
#     seq_region_start = models.IntegerField()
#     seq_region_end = models.IntegerField()
#     band = models.CharField(max_length=120)
#     stain = models.CharField(max_length=120)
#     class Meta:
#         db_table = u'karyotype'
# 
# class Map(models.Model):
#     map_id = models.IntegerField(primary_key=True)
#     map_name = models.CharField(max_length=90)
#     class Meta:
#         db_table = u'map'
# 
# class MappingSession(models.Model):
#     mapping_session_id = models.IntegerField(primary_key=True)
#     old_db_name = models.CharField(max_length=240)
#     new_db_name = models.CharField(max_length=240)
#     old_release = models.CharField(max_length=15)
#     new_release = models.CharField(max_length=15)
#     old_assembly = models.CharField(max_length=60)
#     new_assembly = models.CharField(max_length=60)
#     created = models.DateTimeField()
#     class Meta:
#         db_table = u'mapping_session'
# 
# class MappingSet(models.Model):
#     mapping_set_id = models.IntegerField()
#     schema_build = models.CharField(max_length=60, primary_key=True)
#     class Meta:
#         db_table = u'mapping_set'
# 
# class Marker(models.Model):
#     marker_id = models.IntegerField()
#     display_marker_synonym_id = models.IntegerField(null=True, blank=True)
#     left_primer = models.CharField(max_length=300)
#     right_primer = models.CharField(max_length=300)
#     min_primer_dist = models.IntegerField()
#     max_primer_dist = models.IntegerField()
#     priority = models.IntegerField(null=True, blank=True)
#     type = models.CharField(max_length=42, blank=True)
#     class Meta:
#         db_table = u'marker'
# 
# class MarkerFeature(models.Model):
#     marker_feature_id = models.IntegerField(primary_key=True)
#     marker_id = models.IntegerField()
#     seq_region_id = models.IntegerField()
#     seq_region_start = models.IntegerField()
#     seq_region_end = models.IntegerField()
#     analysis_id = models.IntegerField()
#     map_weight = models.IntegerField(null=True, blank=True)
#     class Meta:
#         db_table = u'marker_feature'
# 
# class MarkerMapLocation(models.Model):
#     marker_id = models.IntegerField(primary_key=True)
#     map_id = models.IntegerField()
#     chromosome_name = models.CharField(max_length=45)
#     marker_synonym_id = models.IntegerField()
#     position = models.CharField(max_length=45)
#     lod_score = models.FloatField(null=True, blank=True)
#     class Meta:
#         db_table = u'marker_map_location'
# 
# class MarkerSynonym(models.Model):
#     marker_synonym_id = models.IntegerField()
#     marker_id = models.IntegerField()
#     source = models.CharField(max_length=60, blank=True)
#     name = models.CharField(max_length=150, blank=True)
#     class Meta:
#         db_table = u'marker_synonym'
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
# class MiscAttrib(models.Model):
#     misc_feature_id = models.IntegerField()
#     attrib_type_id = models.IntegerField()
#     value = models.TextField()
#     class Meta:
#         db_table = u'misc_attrib'
# 
# class MiscFeature(models.Model):
#     misc_feature_id = models.IntegerField(primary_key=True)
#     seq_region_id = models.IntegerField()
#     seq_region_start = models.IntegerField()
#     seq_region_end = models.IntegerField()
#     seq_region_strand = models.IntegerField()
#     class Meta:
#         db_table = u'misc_feature'
# 
# class MiscFeatureMiscSet(models.Model):
#     misc_feature_id = models.IntegerField()
#     misc_set_id = models.IntegerField()
#     class Meta:
#         db_table = u'misc_feature_misc_set'
# 
# class MiscSet(models.Model):
#     misc_set_id = models.IntegerField(primary_key=True)
#     code = models.CharField(unique=True, max_length=75)
#     name = models.CharField(max_length=765)
#     description = models.TextField()
#     max_length = models.IntegerField()
#     class Meta:
#         db_table = u'misc_set'
# 
# class ObjectXref(models.Model):
#     object_xref_id = models.IntegerField()
#     ensembl_id = models.IntegerField()
#     ensembl_object_type = models.CharField(max_length=33)
#     xref_id = models.IntegerField()
#     linkage_annotation = models.CharField(max_length=765, blank=True)
#     analysis_id = models.IntegerField(null=True, blank=True)
#     class Meta:
#         db_table = u'object_xref'
# 
# class PeptideArchive(models.Model):
#     peptide_archive_id = models.IntegerField(primary_key=True)
#     md5_checksum = models.CharField(max_length=96, blank=True)
#     peptide_seq = models.TextField()
#     class Meta:
#         db_table = u'peptide_archive'
# 
# class PredictionExon(models.Model):
#     prediction_exon_id = models.IntegerField(primary_key=True)
#     prediction_transcript_id = models.IntegerField()
#     exon_rank = models.IntegerField()
#     seq_region_id = models.IntegerField()
#     seq_region_start = models.IntegerField()
#     seq_region_end = models.IntegerField()
#     seq_region_strand = models.IntegerField()
#     start_phase = models.IntegerField()
#     score = models.FloatField(null=True, blank=True)
#     p_value = models.FloatField(null=True, blank=True)
#     class Meta:
#         db_table = u'prediction_exon'
# 
# class PredictionTranscript(models.Model):
#     prediction_transcript_id = models.IntegerField(primary_key=True)
#     seq_region_id = models.IntegerField()
#     seq_region_start = models.IntegerField()
#     seq_region_end = models.IntegerField()
#     seq_region_strand = models.IntegerField()
#     analysis_id = models.IntegerField()
#     display_label = models.CharField(max_length=765, blank=True)
#     class Meta:
#         db_table = u'prediction_transcript'
# 
# class ProteinAlignFeature(models.Model):
#     protein_align_feature_id = models.IntegerField(primary_key=True)
#     seq_region_id = models.IntegerField()
#     seq_region_start = models.IntegerField()
#     seq_region_end = models.IntegerField()
#     seq_region_strand = models.IntegerField()
#     hit_start = models.IntegerField()
#     hit_end = models.IntegerField()
#     hit_name = models.CharField(max_length=120)
#     analysis_id = models.IntegerField()
#     score = models.FloatField(null=True, blank=True)
#     evalue = models.FloatField(null=True, blank=True)
#     perc_ident = models.FloatField(null=True, blank=True)
#     cigar_line = models.TextField(blank=True)
#     external_db_id = models.IntegerField(null=True, blank=True)
#     hcoverage = models.FloatField(null=True, blank=True)
#     class Meta:
#         db_table = u'protein_align_feature'
# 
# class ProteinFeature(models.Model):
#     protein_feature_id = models.IntegerField(primary_key=True)
#     translation_id = models.IntegerField()
#     seq_start = models.IntegerField()
#     seq_end = models.IntegerField()
#     hit_start = models.IntegerField()
#     hit_end = models.IntegerField()
#     hit_name = models.CharField(max_length=120)
#     analysis_id = models.IntegerField()
#     score = models.FloatField(null=True, blank=True)
#     evalue = models.FloatField(null=True, blank=True)
#     perc_ident = models.FloatField(null=True, blank=True)
#     external_data = models.TextField(blank=True)
#     class Meta:
#         db_table = u'protein_feature'
# 
# class Qtl(models.Model):
#     qtl_id = models.IntegerField(primary_key=True)
#     trait = models.CharField(max_length=765)
#     lod_score = models.FloatField(null=True, blank=True)
#     flank_marker_id_1 = models.IntegerField(null=True, blank=True)
#     flank_marker_id_2 = models.IntegerField(null=True, blank=True)
#     peak_marker_id = models.IntegerField(null=True, blank=True)
#     class Meta:
#         db_table = u'qtl'
# 
# class QtlFeature(models.Model):
#     seq_region_id = models.IntegerField()
#     seq_region_start = models.IntegerField()
#     seq_region_end = models.IntegerField()
#     qtl_id = models.IntegerField()
#     analysis_id = models.IntegerField()
#     class Meta:
#         db_table = u'qtl_feature'
# 
# class QtlSynonym(models.Model):
#     qtl_synonym_id = models.IntegerField(primary_key=True)
#     qtl_id = models.IntegerField()
#     source_database = models.CharField(max_length=57)
#     source_primary_id = models.CharField(max_length=765)
#     class Meta:
#         db_table = u'qtl_synonym'
# 
# class RepeatConsensus(models.Model):
#     repeat_consensus_id = models.IntegerField(primary_key=True)
#     repeat_name = models.CharField(max_length=765)
#     repeat_class = models.CharField(max_length=300)
#     repeat_type = models.CharField(max_length=120)
#     repeat_consensus = models.TextField(blank=True)
#     class Meta:
#         db_table = u'repeat_consensus'
# 
# class RepeatFeature(models.Model):
#     repeat_feature_id = models.IntegerField(primary_key=True)
#     seq_region_id = models.IntegerField()
#     seq_region_start = models.IntegerField()
#     seq_region_end = models.IntegerField()
#     seq_region_strand = models.IntegerField()
#     repeat_start = models.IntegerField()
#     repeat_end = models.IntegerField()
#     repeat_consensus_id = models.IntegerField()
#     analysis_id = models.IntegerField()
#     score = models.FloatField(null=True, blank=True)
#     class Meta:
#         db_table = u'repeat_feature'


class SeqRegion(models.Model, HasName):
    seq_region_id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=120)
    coord_system = models.ForeignKey(CoordSystem)
    length = models.IntegerField()
    class Meta:
        db_table = u'seq_region'

 
# class SeqRegionAttrib(models.Model):
#     seq_region_id = models.IntegerField()
#     attrib_type_id = models.IntegerField()
#     value = models.TextField()
#     class Meta:
#         db_table = u'seq_region_attrib'
# 
# class SeqRegionMapping(models.Model):
#     external_seq_region_id = models.IntegerField()
#     internal_seq_region_id = models.IntegerField()
#     mapping_set_id = models.IntegerField()
#     class Meta:
#         db_table = u'seq_region_mapping'
# 
# class SimpleFeature(models.Model):
#     simple_feature_id = models.IntegerField(primary_key=True)
#     seq_region_id = models.IntegerField()
#     seq_region_start = models.IntegerField()
#     seq_region_end = models.IntegerField()
#     seq_region_strand = models.IntegerField()
#     display_label = models.CharField(max_length=120)
#     analysis_id = models.IntegerField()
#     score = models.FloatField(null=True, blank=True)
#     class Meta:
#         db_table = u'simple_feature'
# 
# class SplicingEvent(models.Model):
#     splicing_event_id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=402, blank=True)
#     gene_id = models.IntegerField()
#     seq_region_id = models.IntegerField()
#     seq_region_start = models.IntegerField()
#     seq_region_end = models.IntegerField()
#     seq_region_strand = models.IntegerField()
#     type = models.CharField(max_length=12, blank=True)
#     class Meta:
#         db_table = u'splicing_event'
# 
# class SplicingEventFeature(models.Model):
#     splicing_event_feature_id = models.IntegerField(primary_key=True)
#     splicing_event_id = models.IntegerField()
#     exon_id = models.IntegerField(primary_key=True)
#     transcript_id = models.IntegerField()
#     feature_order = models.IntegerField()
#     transcript_association = models.IntegerField()
#     type = models.CharField(max_length=51, blank=True)
#     start = models.IntegerField()
#     end = models.IntegerField()
#     class Meta:
#         db_table = u'splicing_event_feature'
# 
# class SplicingTranscriptPair(models.Model):
#     splicing_transcript_pair_id = models.IntegerField(primary_key=True)
#     splicing_event_id = models.IntegerField()
#     transcript_id_1 = models.IntegerField()
#     transcript_id_2 = models.IntegerField()
#     class Meta:
#         db_table = u'splicing_transcript_pair'
# 
# class StableIdEvent(models.Model):
#     old_stable_id = models.CharField(max_length=384, blank=True)
#     old_version = models.IntegerField(null=True, blank=True)
#     new_stable_id = models.CharField(max_length=384, blank=True)
#     new_version = models.IntegerField(null=True, blank=True)
#     mapping_session_id = models.IntegerField(unique=True)
#     type = models.CharField(unique=True, max_length=33)
#     score = models.FloatField()
#     class Meta:
#         db_table = u'stable_id_event'
# 
# class SupportingFeature(models.Model):
#     exon_id = models.IntegerField(unique=True)
#     feature_type = models.CharField(max_length=63, blank=True)
#     feature_id = models.IntegerField()
#     class Meta:
#         db_table = u'supporting_feature'


class Transcript(HasSeqRegion, HasStableId):
    transcript_id = models.IntegerField(primary_key=True)
    gene = models.ForeignKey('Gene', null=True, blank=True)
    analysis_id = models.IntegerField()
    # seq_region_id = models.IntegerField()
    # seq_region_start = models.IntegerField()
    # seq_region_end = models.IntegerField()
    # seq_region_strand = models.IntegerField()
    display_xref_id = models.IntegerField(null=True, blank=True)
    biotype = models.CharField(max_length=120)
    status = models.CharField(max_length=57, blank=True)
    description = models.TextField(blank=True)
    is_current = models.IntegerField()
    class Meta:
        db_table = u'transcript'
        

# class TranscriptAttrib(models.Model):
#     transcript_id = models.IntegerField()
#     attrib_type_id = models.IntegerField()
#     value = models.TextField()
#     class Meta:
#         db_table = u'transcript_attrib'


class TranscriptStableId(models.Model):
    transcript = models.OneToOneField('Transcript', primary_key=True, related_name='stable_id')
    stable_id = models.CharField(max_length=384)
    version = models.IntegerField(null=True, blank=True)
    created_date = models.DateTimeField()
    modified_date = models.DateTimeField()
    class Meta:
        db_table = u'transcript_stable_id'


# class TranscriptSupportingFeature(models.Model):
#     transcript_id = models.IntegerField(unique=True)
#     feature_type = models.CharField(max_length=63, blank=True)
#     feature_id = models.IntegerField()
#     class Meta:
#         db_table = u'transcript_supporting_feature'
# 
class Translation(HasStableId):
    translation_id = models.IntegerField(primary_key=True)
    transcript = models.OneToOneField('Transcript')
    seq_start = models.IntegerField()
    start_exon = models.ForeignKey('Exon', related_name='start_exon_set')
    seq_end = models.IntegerField()
    end_exon = models.ForeignKey('Exon', related_name='end_exon_set')
    class Meta:
        db_table = u'translation'

# class TranslationAttrib(models.Model):
#     translation_id = models.IntegerField()
#     attrib_type_id = models.IntegerField()
#     value = models.TextField()
#     class Meta:
#         db_table = u'translation_attrib'
 
class TranslationStableId(models.Model):
    translation = models.OneToOneField('Translation', primary_key=True, related_name='stable_id')
    stable_id = models.CharField(max_length=384)
    version = models.IntegerField(null=True, blank=True)
    created_date = models.DateTimeField()
    modified_date = models.DateTimeField()
    class Meta:
        db_table = u'translation_stable_id'
 
# class UnconventionalTranscriptAssociation(models.Model):
#     transcript_id = models.IntegerField()
#     gene_id = models.IntegerField()
#     interaction_type = models.CharField(max_length=69, blank=True)
#     class Meta:
#         db_table = u'unconventional_transcript_association'
# 
# class UnmappedObject(models.Model):
#     unmapped_object_id = models.IntegerField(primary_key=True)
#     type = models.CharField(max_length=48)
#     analysis_id = models.IntegerField()
#     external_db_id = models.IntegerField(null=True, blank=True)
#     identifier = models.CharField(max_length=765)
#     unmapped_reason_id = models.IntegerField()
#     query_score = models.FloatField(null=True, blank=True)
#     target_score = models.FloatField(null=True, blank=True)
#     ensembl_id = models.IntegerField(null=True, blank=True)
#     ensembl_object_type = models.CharField(max_length=33, blank=True)
#     parent = models.CharField(max_length=765, blank=True)
#     class Meta:
#         db_table = u'unmapped_object'
# 
# class UnmappedReason(models.Model):
#     unmapped_reason_id = models.IntegerField(primary_key=True)
#     summary_description = models.CharField(max_length=765, blank=True)
#     full_description = models.CharField(max_length=765, blank=True)
#     class Meta:
#         db_table = u'unmapped_reason'
 
class Xref(models.Model):
    xref_id = models.IntegerField(primary_key=True)
    external_db = models.ForeignKey('ExternalDb')
    dbprimary_acc = models.CharField(unique=True, max_length=120)
    display_label = models.CharField(max_length=384)
    version = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    info_type = models.CharField(max_length=54, blank=True)
    info_text = models.CharField(unique=True, max_length=255, blank=True)
    class Meta:
        db_table = u'xref'

