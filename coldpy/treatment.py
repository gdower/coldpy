
class Treatment:

    def __init__(self,
                 taxon_id,
                 document='',
                 format='',
                 needs_review=''):
        self.taxon_id = taxon_id
        self.document = document
        self.format = format
        self.needs_review = needs_review

    def __str__(self):
        return str(self.taxon_id) + '\t' + \
               str(self.document) + '\t' + \
               str(self.format) + '\n'

    def __repr__(self):
        return {
            'id': self.taxon_id,
            'document': self.document,
            'format': self.format
        }
