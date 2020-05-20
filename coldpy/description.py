
class Description:

    def __init__(self, taxon_id,
                 category='',
                 format='',
                 description='',
                 language='',
                 reference_id='',
                 needs_review=''):
        self.taxon_id = taxon_id
        self.category = category
        self.format = format
        self.description = description
        self.language = language
        self.reference_id = reference_id
        self.needs_review = needs_review

    def __str__(self):
        return str(self.taxon_id) + '\t' + \
               self.category + '\t' + \
               self.format + '\t' + \
               self.description + '\t' + \
               str(self.language) + '\t' + \
               str(self.reference_id) + '\n'

    def __repr__(self):
        return {
            'taxon_id': self.taxon_id,
            'category': self.category,
            'format': self.format,
            'description': self.description,
            'language': self.language,
            'reference_id': self.reference_id
        }
