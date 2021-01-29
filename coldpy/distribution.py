
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


class Distributions:

    def __init__(self, output_tsv):
        self.distributions = []
        self.output_tsv = output_tsv

    def append(self, distribution):
        if isinstance(distribution, Distribution):
            self.distributions.append(distribution)
        else:
            print('Error: distribution must be Distribution type')

    def write_output(self, output_tsv=''):
        if output_tsv == '' and self.output_tsv != '':
            output_tsv = self.output_tsv
        file = open(output_tsv, 'w')
        if len(self.distributions) > 0:
            header = '\t'.join(self.distributions[0].__dict__.keys()) + '\n'
            file.write(header)
        for name in self.distributions:
            row = '\t'.join(str(v) for v in name.__dict__.values()) + '\n'
            file.write(row)
        file.close()
