
class VernacularName:

    def __init__(self,
                 taxon_id,
                 name,
                 transliteration='',
                 language='',
                 country='',
                 area='',
                 sex='',
                 reference_id='',
                 page_reference_id='',
                 needs_review=''):
        self.taxon_id = taxon_id
        self.name = name
        self.transliteration = transliteration
        self.language = language
        self.country = country
        self.area = area
        self.sex = sex
        self.reference_id = reference_id
        self.page_reference_id = page_reference_id
        self.needs_review = needs_review

    def __str__(self):
        return str(self.taxon_id) + '\t' + \
               self.name + '\t' + \
               self.transliteration + '\t' + \
               self.language + '\t' + \
               self.country + '\t' + \
               self.area + '\t' + \
               self.sex + '\t' + \
               str(self.reference_id) + '\t' + \
               str(self.page_reference_id) + '\n'

    def __repr__(self):
        return {
            'taxon_id': self.taxon_id,
            'name': self.name,
            'transliteration': self.transliteration,
            'language': self.language,
            'country': self.country,
            'life_stage': self.area,
            'sex': self.sex,
            'reference_id': self.reference_id,
            'page_reference_id': self.page_reference_id
        }


class VernacularNames:

    def __init__(self, output_tsv):
        self.vernacular_names = []
        self.output_tsv = output_tsv

    def append(self, vernacular_name):
        if isinstance(vernacular_name, VernacularName):
            self.vernacular_names.append(vernacular_name)
        else:
            print('Error: vernacular_name must be VernacularName type')

    def write_output(self, output_tsv=''):
        if output_tsv == '' and self.output_tsv != '':
            output_tsv = self.output_tsv
        file = open(output_tsv, 'w')
        if len(self.vernacular_names) > 0:
            header = '\t'.join(self.vernacular_names[0].__dict__.keys()) + '\n'
            file.write(header)
        for name in self.vernacular_names:
            row = '\t'.join(str(v) for v in name.__dict__.values()) + '\n'
            file.write(row)
        file.close()
