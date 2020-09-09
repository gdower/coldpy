
class Name:

    def __init__(self,
                 id,
                 scientific_name,
                 authorship='',
                 rank='',
                 uninomial='',
                 genus='',
                 infrageneric_epithet='',
                 specific_epithet='',
                 infraspecific_epithet='',
                 cultivar_epithet='',
                 reference_id='',
                 page_reference_id='',
                 published_in_id='',
                 published_in_page='',
                 published_in_year='',
                 basionym_id='',
                 original='',
                 code='',
                 status='',
                 link='',
                 remarks='',
                 output_tsv='',
                 needs_review=''):
        self.id = id
        self.basionym_id = basionym_id
        self.scientific_name = scientific_name
        self.authorship = authorship
        self.rank = rank
        self.uninomial = uninomial
        self.genus = genus
        self.infrageneric_epithet = infrageneric_epithet
        self.specific_epithet = specific_epithet
        self.infraspecific_epithet = infraspecific_epithet
        self.cultivar_epithet = cultivar_epithet
        self.reference_id = reference_id
        self.page_reference_id = page_reference_id
        self.published_in_id = published_in_id
        self.published_in_page = published_in_page
        self.published_in_year = published_in_year
        self.original = original
        self.code = code
        self.status = status
        self.link = link
        self.remarks = remarks
        self.output_tsv = output_tsv
        self.needs_review = needs_review
        self.names = []

        # Backwards compatibility
        if published_in_id != '' and reference_id == '':
            self.reference_id = published_in_id

    def append(self, name):
        if name.isinstance(Name):
            self.names.append(name)
        else:
            print('Error: name must be Name type')

    def write_output(self, output_tsv=''):
        if output_tsv == '' and self.output_tsv != '':
            output_tsv = self.output_tsv
        file = open(output_tsv, 'w')
        for name in self.names:
            file.write(name)
        file.close()

    def __str__(self):
        return str(self.id) + '\t' + \
               str(self.basionym_id) + '\t' + \
               str(self.scientific_name) + '\t' + \
               str(self.authorship) + '\t' + \
               str(self.rank) + '\t' + \
               str(self.genus) + '\t' + \
               str(self.infrageneric_epithet) + '\t' + \
               str(self.specific_epithet) + '\t' + \
               str(self.infraspecific_epithet) + '\t' + \
               str(self.cultivar_epithet) + '\t' + \
               str(self.reference_id) + '\t' + \
               str(self.published_in_page) + '\t' + \
               str(self.published_in_year) + '\t' + \
               str(self.original) + '\t' + \
               str(self.code) + '\t' + \
               str(self.status) + '\t' + \
               str(self.link) + '\t' + \
               str(self.remarks) + '\n'

    def __repr__(self):
        return {
            'id': self.id,
            'basionym_id': self.basionym_id,
            'scientific_name': self.scientific_name,
            'authorship': self.authorship,
            'rank': self.rank,
            'genus': self.genus,
            'infrageneric_epithet': self.infrageneric_epithet,
            'specific_epithet': self.specific_epithet,
            'infraspecific_epithet': self.infraspecific_epithet,
            'cultivar_epithet': self.cultivar_epithet,
            'reference_id': self.published_in_id,
            'published_in_page': self.published_in_page,
            'published_in_year': self.published_in_year,
            'original': self.original,
            'code': self.code,
            'status': self.status,
            'link': self.link,
            'remarks': self.remarks
        }
