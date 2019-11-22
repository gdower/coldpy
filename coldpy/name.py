
class Name:

    def __init__(self,
                 id,
                 scientific_name,
                 authorship='',
                 rank='',
                 genus='',
                 infrageneric_epithet='',
                 specific_epithet='',
                 infraspecific_epithet='',
                 cultivar_epithet='',
                 appended_phrase='',
                 published_in_id='',
                 published_in_page='',
                 published_in_year='',
                 original='',
                 code='',
                 status='',
                 type_status='',
                 type_material='',
                 type_reference_id='',
                 link='',
                 remarks=''):
        self.id = id
        self.scientific_name = scientific_name
        self.authorship = authorship
        self.rank = rank
        self.genus = genus
        self.infrageneric_epithet = infrageneric_epithet
        self.specific_epithet = specific_epithet
        self.infraspecific_epithet = infraspecific_epithet
        self.cultivar_epithet = cultivar_epithet
        self.appended_phrase = appended_phrase
        self.published_in_id = published_in_id
        self.published_in_page = published_in_page
        self.published_in_year = published_in_year
        self.original = original
        self.code = code
        self.status = status
        self.type_status = type_status
        self.type_material = type_material
        self.type_reference_id = type_reference_id
        self.link = link
        self.remarks = remarks

    def __str__(self):
        return str(self.id) + '\t' + \
               str(self.scientific_name) + '\t' + \
               str(self.authorship) + '\t' + \
               str(self.rank) + '\t' + \
               str(self.genus) + '\t' + \
               str(self.infrageneric_epithet) + '\t' + \
               str(self.specific_epithet) + '\t' + \
               str(self.infraspecific_epithet) + '\t' + \
               str(self.cultivar_epithet) + '\t' + \
               str(self.appended_phrase) + '\t' + \
               str(self.published_in_id) + '\t' + \
               str(self.published_in_page) + '\t' + \
               str(self.published_in_year) + '\t' + \
               str(self.original) + '\t' + \
               str(self.code) + '\t' + \
               str(self.status) + '\t' + \
               str(self.type_status) + '\t' + \
               str(self.type_material) + '\t' + \
               str(self.type_reference_id) + '\t' + \
               str(self.link) + '\t' + \
               str(self.remarks) + '\n'

    def __repr__(self):
        return {
            'id': self.id,
            'scientific_name': self.scientific_name,
            'authorship': self.authorship,
            'rank': self.rank,
            'genus': self.genus,
            'infrageneric_epithet': self.infrageneric_epithet,
            'specific_epithet': self.specific_epithet,
            'infraspecific_epithet': self.infraspecific_epithet,
            'cultivar_epithet': self.cultivar_epithet,
            'appended_phrase': self.appended_phrase,
            'published_in_id': self.published_in_id,
            'published_in_page': self.published_in_page,
            'published_in_year': self.published_in_year,
            'original': self.original,
            'code': self.code,
            'status': self.status,
            'type_status': self.type_status,
            'type_reference_id': self.type_reference_id,
            'link': self.link,
            'remarks': self.remarks
        }
