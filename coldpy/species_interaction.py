
class SpeciesInteraction:

    def __init__(self,
                 taxon_id,
                 related_taxon_id='',
                 related_taxon_scientific_name='',
                 type='',
                 reference_id='',
                 page_reference_id='',
                 remarks='',
                 needs_review=''):
        self.taxon_id = taxon_id
        self.related_taxon_id = related_taxon_id
        self.related_taxon_scientific_name = related_taxon_scientific_name
        self.type = type
        self.reference_id = reference_id
        self.page_reference_id = page_reference_id
        self.remarks = remarks
        self.needs_review = needs_review

    def __str__(self):
        return str(self.taxon_id) + '\t' + \
               str(self.related_taxon_id) + '\t' + \
               self.related_taxon_scientific_name + '\t' + \
               self.type + '\t' + \
               str(self.reference_id) + '\t' + \
               str(self.page_reference_id) + '\t' + \
               self.remarks + '\n'

    def __repr__(self):
        return {
            'taxon_id': self.taxon_id,
            'related_taxon_id': self.related_taxon_id,
            'related_taxon_scientific_name': self.related_taxon_scientific_name,
            'type': self.type,
            'reference_id': self.reference_id,
            'page_reference_id': self.page_reference_id,
            'remarks': self.remarks
        }
