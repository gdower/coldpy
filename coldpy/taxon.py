
class Taxon:

    def __init__(self,
                 id,
                 name_id,
                 provisional,
                 according_to,
                 according_to_id,
                 according_to_date,
                 reference_id,
                 extinct,
                 temporal_range_start,
                 temporal_range_end,
                 lifezone,
                 link,
                 remarks,
                 parent_id='',
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
                 kingdom_name=''):

        self.id = id
        self.name_id = name_id
        self.provisional = provisional
        self.according_to = according_to
        self.according_to_id = according_to_id
        self.according_to_date = according_to_date
        self.reference_id = reference_id
        self.extinct = extinct
        self.temporal_range_start = temporal_range_start
        self.temporal_range_end = temporal_range_end
        self.lifezone = lifezone
        self.link = link
        self.remarks = remarks
        self.parent_id = parent_id
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

    def __str__(self):
        return str(self.id) + '\t' + \
               str(self.parent_id) + '\t' + \
               str(self.name_id) + '\t' + \
               str(self.provisional) + '\t' + \
               str(self.according_to) + '\t' + \
               str(self.according_to_id) + '\t' + \
               str(self.according_to_date) + '\t' + \
               str(self.reference_id) + '\t' + \
               str(self.extinct) + '\t' + \
               str(self.temporal_range_start) + '\t' + \
               str(self.temporal_range_end) + '\t' + \
               str(self.lifezone) + '\t' + \
               str(self.link) + '\t' + \
               str(self.remarks) + '\t' + \
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
               str(self.kingdom_name) + '\n'

    def __repr__(self):
        return {'id': self.id,
                'parent_id': self.parent_id,
                'name_id': self.name_id,
                'provisional': self.provisional,
                'according_to': self.according_to,
                'according_to_id': self.according_to_id,
                'according_to_date': self.according_to_date,
                'reference_id': self.reference_id,
                'extinct': self.extinct,
                'temporal_range_start': self.temporal_range_start,
                'temporal_range_end': self.temporal_range_end,
                'lifezone': self.lifezone,
                'link': self.link,
                'remarks': self.remarks,
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
                'kingdom_name': self.kingdom_name
                }
