
class Taxon:

    def __init__(self,
                 id,
                 parent_id,
                 name_id,
                 name_phrase='',
                 according_to_id='',
                 provisional='',
                 scrutinizer='',
                 scrutinizer_id='',
                 scrutinizer_date='',
                 extinct='',
                 temporal_range_start='',
                 temporal_range_end='',
                 lifezone='',
                 reference_id='',
                 page_reference_id='',
                 species_name='',
                 section_name='',
                 subgenus_name='',
                 genus_name='',
                 subtribe_name='',
                 tribe_name='',
                 subfamily_name='',
                 family_name='',
                 superfamily_name='',
                 suborder_name='',
                 order_name='',
                 subclass_name='',
                 class_name='',
                 subphylum_name='',
                 phylum_name='',
                 kingdom_name='',
                 link='',
                 remarks='',
                 needs_review=''):

        self.id = id
        self.parent_id = parent_id
        self.name_id = name_id
        self.name_phrase = name_phrase
        self.according_to_id = according_to_id
        self.provisional = provisional
        self.scrutinizer = scrutinizer
        self.scrutinizer_id = scrutinizer_id
        self.scrutinizer_date = scrutinizer_date
        self.extinct = extinct
        self.temporal_range_start = temporal_range_start
        self.temporal_range_end = temporal_range_end
        self.lifezone = lifezone
        self.reference_id = reference_id
        self.page_reference_id = page_reference_id
        self.species_name = species_name
        self.section_name = section_name
        self.subgenus_name = subgenus_name
        self.genus_name = genus_name
        self.subtribe_name = subtribe_name
        self.tribe_name = tribe_name
        self.subfamily_name = subfamily_name
        self.family_name = family_name
        self.superfamily_name = superfamily_name
        self.suborder_name = suborder_name
        self.order_name = order_name
        self.subclass_name = subclass_name
        self.class_name = class_name
        self.subphylum_name = subphylum_name
        self.phylum_name = phylum_name
        self.kingdom_name = kingdom_name
        self.link = link
        self.remarks = remarks
        self.needs_review = needs_review

    def __str__(self):
        return str(self.id) + '\t' + \
               str(self.parent_id) + '\t' + \
               str(self.name_id) + '\t' + \
               str(self.name_phrase) + '\t' + \
               str(self.according_to_id) + '\t' + \
               str(self.provisional) + '\t' + \
               str(self.scrutinizer) + '\t' + \
               str(self.scrutinizer_id) + '\t' + \
               str(self.scrutinizer_date) + '\t' + \
               str(self.extinct) + '\t' + \
               str(self.temporal_range_start) + '\t' + \
               str(self.temporal_range_end) + '\t' + \
               str(self.lifezone) + '\t' + \
               str(self.reference_id) + '\t' + \
               str(self.page_reference_id) + '\t' + \
               str(self.species_name) + '\t' + \
               str(self.section_name) + '\t' + \
               str(self.subgenus_name) + '\t' + \
               str(self.genus_name) + '\t' + \
               str(self.subtribe_name) + '\t' + \
               str(self.tribe_name) + '\t' + \
               str(self.subfamily_name) + '\t' + \
               str(self.family_name) + '\t' + \
               str(self.superfamily_name) + '\t' + \
               str(self.suborder_name) + '\t' + \
               str(self.order_name) + '\t' + \
               str(self.subclass_name) + '\t' + \
               str(self.class_name) + '\t' + \
               str(self.subphylum_name) + '\t' + \
               str(self.phylum_name) + '\t' + \
               str(self.kingdom_name) + '\t' + \
               str(self.link) + '\t' + \
               str(self.remarks) + '\n'

    def __repr__(self):
        return {'id': self.id,
                'parent_id': self.parent_id,
                'name_id': self.name_id,
                'name_phrase': self.name_phrase,
                'according_to_id': self.according_to_id,
                'provisional': self.provisional,
                'scrutinizer': self.scrutinizer,
                'scrutinizer_id': self.scrutinizer_id,
                'scrutinizer_date': self.scrutinizer_date,
                'extinct': self.extinct,
                'temporal_range_start': self.temporal_range_start,
                'temporal_range_end': self.temporal_range_end,
                'lifezone': self.lifezone,
                'reference_id': self.reference_id,
                'page_reference_id': self.page_reference_id,
                'species_name': self.species_name,
                'section_name': self.section_name,
                'subgenus_name': self.subgenus_name,
                'genus_name': self.genus_name,
                'subtribe_name': self.subtribe_name,
                'tribe_name': self.tribe_name,
                'subfamily_name': self.subfamily_name,
                'family_name': self.family_name,
                'superfamily_name': self.superfamily_name,
                'suborder_name': self.suborder_name,
                'order_name': self.order_name,
                'subclass_name': self.subclass_name,
                'class_name': self.class_name,
                'subphylum_name': self.subphylum_name,
                'phylum_name': self.phylum_name,
                'kingdom_name': self.kingdom_name,
                'link': self.link,
                'remarks': self.remarks,
                }
