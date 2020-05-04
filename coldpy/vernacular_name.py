
class VernacularName:

    def __init__(self,
                 taxon_id,
                 name,
                 transliteration='',
                 language='',
                 country='',
                 life_stage='',
                 sex='',
                 reference_id=''):
        self.taxon_id = taxon_id
        self.name = name
        self.transliteration = transliteration
        self.language = language
        self.country = country
        self.life_stage = life_stage
        self.sex = sex
        self.reference_id = reference_id

    def __str__(self):
        return str(self.taxon_id) + '\t' + \
               self.name + '\t' + \
               self.transliteration + '\t' + \
               self.language + '\t' + \
               self.country + '\t' + \
               self.life_stage + '\t' + \
               self.sex + '\t' + \
               str(self.reference_id) + '\n'

    def __repr__(self):
        return {
            'taxon_id': self.taxon_id,
            'name': self.name,
            'transliteration': self.transliteration,
            'language': self.language,
            'country': self.country,
            'life_stage': self.life_stage,
            'sex': self.sex,
            'reference_id': self.reference_id
        }
