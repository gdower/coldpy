
class Synonym:

    def __init__(self,
                 taxon_id,
                 name_id,
                 status='synonym',
                 reference_id='',
                 remarks=''):
        self.taxon_id = taxon_id
        self.name_id = name_id
        self.status = status
        self.reference_id = reference_id
        self.remarks = remarks

    def __str__(self):
        return str(self.taxon_id) + '\t' + \
               str(self.name_id) + '\t' + \
               self.status + '\t' + \
               str(self.reference_id) + '\t' + \
               self.remarks + '\n'

    def __repr__(self):
        return {
            'taxon_id': self.taxon_id,
            'name_id': self.name_id,
            'status': self.status,
            'reference_id': self.reference_id,
            'remarks': self.remarks
        }
