
class Synonym:

    def __init__(self,
                 taxon_id,
                 name_id,
                 id='',
                 name_phrase='',
                 according_to_id='',
                 status='synonym',
                 reference_id='',
                 page_reference_id='',
                 link='',
                 remarks='',
                 needs_review=''):
        self.id = id
        self.taxon_id = taxon_id
        self.name_id = name_id
        self.name_phrase = name_phrase
        self.according_to_id = according_to_id
        self.status = status
        self.reference_id = reference_id
        self.page_reference_id = page_reference_id
        self.link = link
        self.remarks = remarks
        self.needs_review = needs_review

        # Possibly a bad idea
        if id == '':
            self.id = '-'.join([taxon_id, name_id])

    def __str__(self):
        return str(self.id) + '\t' + \
               str(self.taxon_id) + '\t' + \
               str(self.name_id) + '\t' + \
               self.name_phrase + '\t' + \
               str(self.according_to_id) + '\t' + \
               self.status + '\t' + \
               str(self.reference_id) + '\t' + \
               str(self.page_reference_id) + '\t' + \
               self.link + '\t' + \
               self.remarks + '\n'

    def __repr__(self):
        return {
            'id': self.id,
            'taxon_id': self.taxon_id,
            'name_id': self.name_id,
            'name_phrase': self.name_phrase,
            'according_to_id': self.according_to_id,
            'status': self.status,
            'reference_id': self.reference_id,
            'page_reference_id': self.page_reference_id,
            'link': self.link,
            'remarks': self.remarks
        }
