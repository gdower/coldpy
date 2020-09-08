
class Distribution:

    def __init__(self,
                 taxon_id,
                 area,
                 gazetteer='',
                 status='',
                 reference_id='',
                 page_reference_id='',
                 needs_review=''):
        self.taxon_id = taxon_id
        self.area = area
        self.gazetteer = gazetteer
        self.status = status
        self.reference_id = reference_id
        self.page_reference_id = page_reference_id
        self.needs_review = needs_review

    def __str__(self):
        return str(self.taxon_id) + '\t' + \
               self.area + '\t' + \
               self.gazetteer + '\t' + \
               self.status + '\t' + \
               str(self.reference_id) + '\t' + \
               str(self.page_reference_id) + '\n'

    def __repr__(self):
        return {
            'taxon_id': self.taxon_id,
            'area': self.area,
            'gazetteer': self.gazetteer,
            'status': self.status,
            'reference_id': self.reference_id,
            'page_reference_id': self.page_reference_id
        }
